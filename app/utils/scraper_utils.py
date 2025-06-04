from crawl4ai import BrowserConfig

def get_browser_config() -> BrowserConfig:
    return BrowserConfig(
            browser_type = "chromium",
            headless = True,
            verbose = True,
            user_agent_mode = "random",
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
            )
