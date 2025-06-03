from crawl4ai import BrowserConfig, LLMExtractionStrategy

def get_browser_config() -> BrowserConfig:
    return BrowserConfig(browser_type="chromium",headless=True,verbose=True)