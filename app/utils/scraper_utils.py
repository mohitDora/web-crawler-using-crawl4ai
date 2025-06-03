from crawl4ai import BrowserConfig

def get_browser_config() -> BrowserConfig:
    return BrowserConfig(browser_type="chromium",headless=True,verbose=True)