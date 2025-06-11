from crawl4ai import BrowserConfig

def get_browser_config() -> BrowserConfig:
    return BrowserConfig(
            browser_type = "chromium",
            headless = True,
            verbose = True,
            user_agent_mode = "random",
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            # --- Proxy config example (uncomment and rotate as needed) ---
            # proxy_config={
            #     "server": "http://proxy.example.com:8080",
            #     "username": "myuser",
            #     "password": "mypass",
            # },
            # --- Persistent context for cookies/session ---
            use_persistent_context=True,
            # --- Browser-like headers ---
            headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Upgrade-Insecure-Requests": "1",
                "DNT": "1",
            },
            )
