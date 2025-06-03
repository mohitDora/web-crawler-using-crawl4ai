import asyncio
from services.scraper import scrape
import json

res=asyncio.run(scrape("https://www.google.com/search?q=bellyful+restaurant+sambalpur"))

print(json.dumps(res.get("external",[]),indent=2))
