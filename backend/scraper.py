import os
from dotenv import load_dotenv
from datetime import date, timedelta
from fredapi import Fred
from playwright.sync_api import sync_playwright
from config import COUNTRIES_CONFIG
from supabase import create_client, Client

# --- SETUP ---
FRED_API_KEY =  os.getenv("FRED_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --- INITIALIZE CLIENTS ---
fred = Fred(api_key=FRED_API_KEY)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- CHECKPOINTING FUNCTIONS ---
def get_scraped_today():
    """Reads the log file to see which countries were scraped today."""
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
    
    today_str = str(date.today())
    scraped_today = set()
    for line in lines:
        if line.strip().startswith(today_str):
            try:
                country_code = line.strip().split(',')[1]
                scraped_today.add(country_code)
            except IndexError:
                continue # Skip malformed lines
    return scraped_today

def log_successful_scrape(country_code):
    """Adds a country's success to the log file for today."""
    with open(LOG_FILE, 'a') as f:
        f.write(f"{date.today()},{country_code}\n")

# --- HELPER FUNCTIONS ---
def get_fred_yoy_change(series_id, is_quarterly=False):
    """Calculates YoY change for FRED level data (CPI, GDP)."""
    try:
        start_date = date.today() - timedelta(days=500)
        series = fred.get_series(series_id, observation_start=start_date).dropna()
        periods = 4 if is_quarterly else 12
        if len(series) < periods + 1:
            print(f"  -> Not enough data for YoY calc on {series_id}")
            return None
        latest = series.iloc[-1]
        previous = series.iloc[-1 - periods]
        return round(((latest - previous) / previous) * 100, 2)
    except Exception as e:
        print(f"  -> FRED YoY Error for {series_id}: {e}")
        return None

def get_fred_latest_value(series_id, convert_to_billions=False):
    """Fetches latest value for FRED rates or converts trade balance units."""
    try:
        value = fred.get_series_latest_release(series_id).iloc[0]
        if convert_to_billions:
            return round(value / 1000, 2) # From Millions to Billions
        return round(value, 2)
    except Exception as e:
        print(f"  -> FRED Latest Val Error for {series_id}: {e}")
        return None

def scrape_with_playwright(page, url, selector):
    """Generic Playwright scraping function."""
    try:
        page.goto(url, timeout=30000, wait_until='domcontentloaded')
        element = page.wait_for_selector(selector, timeout=15000)
        text = element.inner_text()
        return float(''.join(filter(lambda x: x in '0123456789.-', text)))
    except Exception as e:
        print(f"  -> Playwright Error for {url}: {e}")
        return None

# --- MAIN SCRAPER ---
def run_updater():
    print("--- Starting Efficient Scraper ---")
    scraped_today = get_scraped_today()
    print(f"Countries already scraped today: {scraped_today or 'None'}")
    
    countries_to_scrape = [c for c in COUNTRIES_CONFIG if c['country_code'] not in scraped_today]
    if not countries_to_scrape:
        print("\n--- All countries are up to date. Exiting. ---")
        return

    all_country_data = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for country in countries_to_scrape:
            country_code = country['country_code']
            print(f"\n--- Processing {country['country_name']} ---")
            data = {
                "CountryCode_ISO2": country_code,
                "CountryName": country['country_name'],
                "LastUpdated_Date": str(date.today())
            }

            # Process each metric with explicit, safe logic
            if 'policy_rate' in country:
                config = country['policy_rate']
                if config['source'] == 'fred_api':
                    data['PolicyRate_UpperBound'] = get_fred_latest_value(config['series_id'])
                elif config['source'] == 'web_scrape':
                    data['PolicyRate_UpperBound'] = scrape_with_playwright(page, config['url'], config['selector'])

            if 'gdp_growth' in country:
                config = country['gdp_growth']
                if config['source'] == 'fred_api':
                    data['GDP_Growth_YoY'] = get_fred_yoy_change(config['series_id'], is_quarterly=True)
                elif config['source'] == 'web_scrape':
                    data['GDP_Growth_YoY'] = scrape_with_playwright(page, config['url'], config['selector'])
            
            if 'inflation_rate' in country:
                config = country['inflation_rate']
                if config['source'] == 'fred_api':
                    data['Inflation_CPI_YoY'] = get_fred_yoy_change(config['series_id'])
                elif config['source'] == 'web_scrape':
                    data['Inflation_CPI_YoY'] = scrape_with_playwright(page, config['url'], config['selector'])

            if 'unemployment_rate' in country:
                config = country['unemployment_rate']
                if config['source'] == 'fred_api':
                    data['Unemployment_Rate'] = get_fred_latest_value(config['series_id'])
                elif config['source'] == 'web_scrape':
                    data['Unemployment_Rate'] = scrape_with_playwright(page, config['url'], config['selector'])
            
            if 'bond_yield' in country:
                config = country['bond_yield']
                if config['source'] == 'fred_api':
                    data['BondYield_10Y'] = get_fred_latest_value(config['series_id'])
                elif config['source'] == 'web_scrape':
                    data['BondYield_10Y'] = scrape_with_playwright(page, config['url'], config['selector'])
            
            if 'trade_balance' in country:
                config = country['trade_balance']
                if config['source'] == 'fred_api':
                    data['TradeBalance_USD'] = get_fred_latest_value(config['series_id'], convert_to_billions=True)
                elif config['source'] == 'web_scrape':
                    data['TradeBalance_USD'] = scrape_with_playwright(page, config['url'], config['selector'])

            # Print what was successfully gathered for this country
            for key, val in data.items():
                if key not in ["CountryCode_ISO2", "CountryName", "LastUpdated_Date"] and val is not None:
                    print(f"  ✅ {key}: {val}")
            
            all_country_data.append(data)
            log_successful_scrape(country_code)
        
        browser.close()

    if all_country_data:
        print("\n--- Saving newly scraped data to Supabase ---")
        supabase.table('country_data').upsert(all_country_data).execute()
        print("✅ Batch update to Supabase complete.")
    else:
        print("\n--- No new data to save to Supabase. ---")

if __name__ == "__main__":
    run_updater()


