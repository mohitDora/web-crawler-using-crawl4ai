# import asyncio
# from services.scraper import scrape
# import json

# res=asyncio.run(scrape("https://www.google.com/search?q=bellyful+restaurant+sambalpur"))

# print(json.dumps(res.get("external",[]),indent=2))


# app/main.py
import asyncio
import sys
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import HttpUrl
from app.services.scraper import scrape

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

@app.get("/scrape")
async def scrape_url(url: HttpUrl = Query(..., description="URL to scrape")):
    result = await scrape(str(url))
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to scrape URL")
    return JSONResponse(content=result, status_code=200)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Run via: uvicorn app.main:app --reload
