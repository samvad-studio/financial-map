from datetime import date
from playwright.sync_api import sync_playwright
from supabase import create_client, Client

# --- SETUP: Add your Supabase credentials ---
SUPABASE_URL = "https://nujyopdmqolfvvzggyud.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im51anlvcGRtcW9sZnZ2emdneXVkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NzQ3NjIxMSwiZXhwIjoyMDczMDUyMjExfQ.WqBMuGap8oYrjhbVguXiPFIyeyhEVEk2KbwdN5mTEHk" 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def scrape_and_update():
    print("--- Starting scraper for upper bound rate ---")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            target_url = "https://www.federalreserve.gov/economy-at-a-glance-policy-rate.htm"
            page.goto(target_url, timeout=30000)

            rate_selector = "div.fomc-latest-data-value"
            rate_element = page.wait_for_selector(rate_selector)
            rate_text = rate_element.inner_text()
            browser.close()

            upper_range_str = rate_text.split('to')[-1].strip()
            upper_bound = float(upper_range_str.replace("-1/4", ".25").replace("-1/2", ".5").replace("-3/4", ".75").replace("%", ""))
            print(f"✅ Scraped Rate (Upper Bound): {upper_bound}%")

            data_to_upsert = {
                "CountryCode_ISO2": "US",
                "CountryName": "United States",
                "PolicyRate_UpperBound": upper_bound,
                "LastUpdated_Date": str(date.today())
            }

            supabase.table('country_data').upsert(data_to_upsert).execute()
            print("✅ Successfully saved upper bound to Supabase.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    scrape_and_update()
    

