from datetime import datetime

import httpx

from ..domain import WebPage

# A general scraper logic to isolate the choice of webscraper, Selenium or BeautifulSoup


class WebRetriever:

    url: str 
    headers: dict

    def __init__(self, url: str):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_site(self) -> WebPage:
        try:
            result = httpx.get(self.url, headers=self.headers, verify=False)
            return WebPage(self.url, datetime.now(), result.text)
        except Exception:
            return WebPage(self.url, datetime.now(), result)



