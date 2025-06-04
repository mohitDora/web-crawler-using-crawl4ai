from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
from utils.scraper_utils import get_browser_config
import uuid

async def scrape(url: str):
    browser_config = get_browser_config()
    run_config=CrawlerRunConfig(session_id=uuid.uuid4())
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=url,
            config=run_config
        )
        return result.links if result.success else None

