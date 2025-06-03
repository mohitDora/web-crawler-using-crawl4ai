import asyncio
import sys
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import HttpUrl
from app.services.scraper import scrape
import json

app = FastAPI()

@app.get("/scrape")
async def scrape_url(url: HttpUrl = Query(..., description="URL to scrape")):
    result = await scrape(str(url))
    result = await scrape("https://www.google.com/search?q=bellyful+restaurant+sambalpur")
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to scrape URL")
    return JSONResponse(content=result.get("external",[]), status_code=200)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
