COUNTRIES_CONFIG = [
    {
        "country_name": "United States",
        "country_code": "US",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "GDPC1"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPIAUCSL"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "FEDFUNDS"
            },           # Federal Funds Target Range - Upper Bound
        "unemployment_rate": {
            "source": "fred_api",
            "series_id": "UNRATE"
            },         # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "DGS10"
            },              # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "BOPGSTB"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Japan",
        "country_code": "JP",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "JPNRGDPEXP"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "web_scrape",
            "url": "https://www.stat.go.jp/english/",
            "selector": "#top_open_data > ul > li:nth-child(2) > div > div > a > span"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01JPM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRUN64TTJPM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01JPM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01JPQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Germany",
        "country_code": "DE",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "CLVMNACSCAB1GQDE"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01DEM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "ECBDFR"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTDEM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01DEM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01DEM667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "United Kingdom",
        "country_code": "GB",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "UKNGDP"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01GBM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate",
            "selector": "#main-content > section:nth-child(3) > div > div.grid.grid--flex > div:nth-child(1) > div > h2 > span"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTGBM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01GBM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01GBQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "France",
        "country_code": "FR",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "CLVMNACSCAB1GQFR"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01FRM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "ECBDFR"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTFRM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01FRM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "FRAXTNTVA01CXMLQ"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Italy",
        "country_code": "IT",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "CLVMNACSCAB1GQIT"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01ITM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "ECBDFR"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTITM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01ITM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01ITQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Canada",
        "country_code": "CA",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCCAQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01CAM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01CAM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRUNTTTTCAM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01CAM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01CAQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "China",
        "country_code": "CN",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": ""
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01CNM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01CNM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": ""
            },           # Unemployment Rate
        "bond_yield": {
            "source": "web_scrape",
            "url": "https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/more?locale=en_US",
            "selector": "#gjqxData > table > tbody > tr:nth-child(2) > td:nth-child(8)"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01CNM667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "India",
        "country_code": "IN",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRNSAXDCINQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01INM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01INM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": ""
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "INDIRLTLT01STM"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01INQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Brazil",
        "country_code": "BR",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCBRQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01BRM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01BRM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url": "https://www.ibge.gov.br/en/indicators.html?view=default",
            "selector": "body > main > section > div.envolve_conteudo > div.indicadores-destaque > div > div:nth-child(4) > p.indicador-value"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "INTGSTBRM193N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01BRQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Russia",
        "country_code": "RU",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRNSAXDCRUQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "web_scrape",
            "url": "https://www.cbr.ru/eng/",
            "selector": "#content > div > div > div > div.home-main > div.home-main_aside > div > div:nth-child(2) > div.main-indicator_value"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.cbr.ru/eng/",
            "selector": "#content > div > div > div > div.home-main > div.home-main_aside > div > div:nth-child(3) > div.main-indicator_value"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url": "https://eng.rosstat.gov.ru",
            "selector": "body > main > section:nth-child(2) > div > div > div > div > div:nth-child(1) > div > div.card-universal__main > div > div > div.indicators__main > div:nth-child(6) > div:nth-child(2) > div.indicators__data"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "web_scrape",
            "url": "https://www.worldgovernmentbonds.com/bond-historical-data/russia/10-years/",
            "selector": "#post-7 > div.entry-content > div:nth-child(3) > div > div.summary-value.borsaInverso > span > span.summary-value-number"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01RUM667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "South Africa",
        "country_code": "ZA",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCZAQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01ZAM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/current-market-rates",
            "selector": "body > div.root.responsivegrid > div > div.marketrates.aem-GridColumn.aem-GridColumn--default--12 > div.currentmarketrates.api-marketrate > div.currentmarketrates__table.table-responsive.table-sm.table-borderless > table > tbody > tr:nth-child(3) > td.mval"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRUN64TTZAQ156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01ZAM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01ZAQ667S"
            },            # Trade Balance in Goods and Services
    }, 
    {
        "country_name": "Australia",
        "country_code": "AU",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCAUQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01AUQ659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": "IRSTCI01AUM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRUNTTTTAUM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01AUM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01AUQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Argentina",
        "country_code": "AR",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCARQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "ARGCPALTT01GYM"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id": ""
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url":"https://www.indec.gob.ar",
            "selector": "#content > div:nth-child(1) > div > div > div > div > div:nth-child(2) > a > div > div.tooltip-resp > div.font-1"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": ""
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "ARGXTNTVA01CXMLSAM"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Indonesia",
        "country_code": "ID",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCIDQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPALTT01IDM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url":"https://www.bi.go.id/en/default.aspx",
            "selector": "#DeltaPlaceHolderMain > div:nth-child(3) > div > div > div:nth-child(1) > div > a > h2"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url":"https://www.bps.go.id/en",
            "selector": "body > div.max-\[320px\]\:h-\[70vh\].h-\[50vh\].md\:h-\[40vh\].lg\:h-\[65vh\].\32 xl\:h-\[50vh\].min-h-fit.mb-\[calc\(6vh\+1\.5rem\)\].md\:mb-\[calc\(8vh\+1\.5rem\)\].\32 xl\:mb-\[calc\(10vh\+1\.5rem\)\] > div > div.w-full.relative.bottom-\[-8vh\].\32 xl\:bottom-\[-10vh\] > div > div.h-fit.w-full.flex.items-center.relative > div.swiper.swiper-initialized.swiper-horizontal.h-full.w-full > div > div:nth-child(5) > a > h3"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "web_scrape",
            "url": "https://asianbondsonline.adb.org/indonesia/",
            "selector": "#market-at-a-glance > div > div.col-lg-5 > div:nth-child(2) > table > tbody:nth-child(5) > tr > td:nth-child(2)"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "ARGXTNTVA01CXMLSAM"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Mexico",
        "country_code": "MX",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCMXQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "web_scrape",
            "url":"https://en.www.inegi.org.mx/temas/inpc/",
            "selector": "#valorgraf_gral0"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url":"",
            "selector": ""
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTMXM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01MXM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01MXM667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Saudi Arabia",
        "country_code": "SA",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCSAQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "SAUCPALTT01GYM"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url":"https://www.sama.gov.sa/en-US/Pages/default.aspx",
            "selector": "#ctl00_ctl50_g_2ac22520_e79f_4dc2_94eb_c3b03d5ad702 > div.Economicbody > div:nth-child(4) > div.percentage-item > span"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url": "https://www.stats.gov.sa/en/home",
            "selector": "#portlet_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_yuef > div > div > div > div > div > div.owl-carousel.dga-dots.remove-dots.owl-loaded.owl-drag > div.owl-stage-outer > div > div:nth-child(3) > div > div > div.card-body.d-flex.gap-3.justify-content-between.flex-column.align-items-center > h2"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "",
            "series_id": ""
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "SAUXTNTVA01CXMLSAM"
            },            # Trade Balance in Goods and Services
    }, 
    {
        "country_name": "South Korea",
        "country_code": "KR",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCKRQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01KRM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "fred_api",
            "series_id":"IRSTCI01KRM156N"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRUNTTTTKRM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": "IRLTLT01KRM156N"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01KRQ667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Turkey",
        "country_code": "TR",
        "gdp_growth": {
            "source": "fred_api",
            "series_id": "NGDPRSAXDCTRQ"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "fred_api",
            "series_id": "CPGRLE01KRM659N"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.tcmb.gov.tr/wps/wcm/connect/en/tcmb+en",
            "selector": "#hr-bv"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "fred_api",
            "series_id": "LRHUTTTTTRM156S"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": ""
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": "XTNTVA01TRM667S"
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Thailand",
        "country_code": "TH",
        "gdp_growth": {
            "source": "web_scrape",
            "url": "https://www.nesdc.go.th/en/",
            "selector": "#content > div:nth-child(1) > div > div.elementor-element.elementor-element-cb13ce9.e-con-full.home-report-section-wrap.e-flex.e-con.e-parent.e-lazyloaded > div.elementor-element.elementor-element-faa8b69.e-con-full.home-report-section.e-flex.e-con.e-child > div > div > div.elementor-element.elementor-element-a3e99a3.elementor-widget__width-inherit.animated-slow.elementor-widget.elementor-widget-shortcode.animated.fadeInUp > div > div > div.home-report-wrapper > div:nth-child(1) > div > div > div.home-report-content-panel-1 > div > div > div.report-col-1 > div > div.data-value > span"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "web_scrape",
            "url": "https://www.bot.or.th/en/home.html",
            "selector": "#container-c84cefbc55 > div > div > div > div > div.wtc-description > table > tbody > tr:nth-child(3) > td:nth-child(1)"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.bot.or.th/en/home.html",
            "selector": "#container-6b2c2c8d0d > div > div > bot-dashboard-widget > div > div > div.description > table > tbody > tr:nth-child(2) > td"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url": "https://www.nesdc.go.th/en/",
            "selector": "#content > div:nth-child(1) > div > div.elementor-element.elementor-element-cb13ce9.e-con-full.home-report-section-wrap.e-flex.e-con.e-parent.e-lazyloaded > div.elementor-element.elementor-element-faa8b69.e-con-full.home-report-section.e-flex.e-con.e-child > div > div > div.elementor-element.elementor-element-a3e99a3.elementor-widget__width-inherit.animated-slow.elementor-widget.elementor-widget-shortcode.animated.fadeInUp > div > div > div.home-report-wrapper > div.home-social-report-section.homereport-section > div > div.home-report-content-panel-1 > div > div > div.report-col-1 > div > div.data-value > span"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "fred_api",
            "series_id": ""
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "fred_api",
            "series_id": ""
            },            # Trade Balance in Goods and Services
    },
    {
        "country_name": "Malaysia",
        "country_code": "MY",
        "gdp_growth": {
            "source": "web_scrape",
            "url": "https://open.dosm.gov.my",
            "selector": "#__next > div.__variable_19640c.font-sans > div.flex.min-h-screen.flex-col > div.flex.flex-grow.flex-col > div > div:nth-child(2) > div > section:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > div.space-y-0\.5 > span > p.text-2xl.font-medium"
            },    # Real GDP Growth, YoY
        "inflation_rate": {
            "source": "web_scrape",
            "url": "https://open.dosm.gov.my",
            "selector": "#__next > div.__variable_19640c.font-sans > div.flex.min-h-screen.flex-col > div.flex.flex-grow.flex-col > div > div:nth-child(2) > div > section:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(3) > div.space-y-0\.5 > span > p.text-2xl.font-medium"
            },          # CPI, YoY will be calculated
        "policy_rate": {
            "source": "web_scrape",
            "url": "https://www.bnm.gov.my",
            "selector": "#portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_rqG2eQryrjsK > div > div.portlet-content-container > div > div > div > section > div > div > div > div.col-lg-3.d-flex.flex-column.flex-sm-row.flex-md-row.flex-lg-column.justify-content-center.mb-3.text-light > div:nth-child(1) > div > span.display-4.mb-0"
            },     # Federal Funds Target Range - Upper Bound
       "unemployment_rate": {
            "source": "web_scrape",
            "url": "https://open.dosm.gov.my",
            "selector": "#__next > div.__variable_19640c.font-sans > div.flex.min-h-screen.flex-col > div.flex.flex-grow.flex-col > div > div:nth-child(2) > div > section:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(4) > div.space-y-0\.5 > span > p.text-2xl.font-medium"
            },           # Unemployment Rate
        "bond_yield": {
            "source": "web_scrape",
            "url": "https://financialmarkets.bnm.gov.my",
            "selector": "#main-header > div:nth-child(2) > div > div > div:nth-child(2) > table > tbody > tr > td.text-right > div"
            },                  # 10-Year Treasury Yield
        "trade_balance": {
            "source": "web_scrape",
            "url": "https://metsonline.dosm.gov.my",
            "selector": "#signup > div > div.container > div > div.custom-box > div > div:nth-child(4) > div > div > div.text-white > h3"
            },            # Trade Balance in Goods and Services
    },
    ]