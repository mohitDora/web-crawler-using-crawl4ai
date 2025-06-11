from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import CrawlerRunConfig
from app.utils.scraper_utils import get_browser_config
import uuid
import asyncio
import random

async def scrape(url: str):
    # Add a random delay to mimic human browsing
    await asyncio.sleep(random.uniform(2, 5))
    browser_config = get_browser_config()
    run_config=CrawlerRunConfig(session_id=uuid.uuid4())
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=url,
            config=run_config
        )
        return result.links if result.success else None

