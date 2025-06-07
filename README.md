# FastAPI Web Crawler using Crawl4AI

This project is a web scraping API built with FastAPI, leveraging [Crawl4AI](https://github.com/scaleupstack/crawl4ai) and Playwright for robust, headless browser-based crawling. It exposes endpoints to scrape external URLs and retrieve links.

## Features
- **/scrape** endpoint: Scrape a given URL and return external links.
- **/health** endpoint: Health check for the API.
- Asynchronous scraping using Crawl4AI and Playwright (Chromium, headless).

## Requirements
- Docker (recommended)
- Or: Python 3.11+, pip

## Quick Start (Docker)

1. **Build the Docker image:**
   ```sh
   docker build -t fastapi-crawler .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8000:8000 fastapi-crawler
   ```
3. **Access the API:**
   Open [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.

## Local Development (without Docker)

1. **Install dependencies:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   python -m playwright install --with-deps
   ```
2. **Run the app:**
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints

### `GET /scrape`
Scrape a given URL and return external links.

**Query Parameters:**
- `url` (string, required): The URL to scrape.

**Example:**
```
GET http://localhost:8000/scrape?url=https://example.com
```

**Response:**
- `200 OK`: List of external links found on the page.
- `500`: If scraping fails.

### `GET /health`
Health check endpoint.

**Response:**
```
{"status": "ok"}
```

## Project Structure
```
app/
  main.py            # FastAPI app and endpoints
  services/
    scraper.py       # Scraping logic using Crawl4AI
  utils/
    scraper_utils.py # Browser config for Playwright
requirements.txt     # Python dependencies
Dockerfile           # Container setup
```

## Notes
- The crawler uses Chromium in headless mode with a random user agent.
- Playwright browser dependencies are installed automatically in Docker and local setup.
