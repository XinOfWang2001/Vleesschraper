import unittest as ut
from datetime import datetime

import mock

from src.domain import WebPage, MeatProduct
from src.logic import AlbertMenuParser, WebRetriever


class TestParser(ut.TestCase):

    def test_parser(self):
        location_html = "src/tests/html/product.html"
        html = ""
        with open(location_html) as file:
            html = file.read()
        url = "local"
        retriever = WebRetriever(url)
        retriever.scrape_site = mock.Mock(return_value=WebPage(url, 
                                                             date_time=datetime.now(), 
                                                             html_content=html))
        albert_scraper = AlbertMenuParser(retriever)
        result: list[MeatProduct] = albert_scraper.parse()
        self.assertEqual(36, len(result))

        # Just pick the first one just to test.
        first = result.pop()
        self.assertEqual("AH Scharrel kipfilet blokjes", first.full_title)
        self.assertEqual(5.49, first.current_price)
        self.assertEqual(300, first.weight)

if __name__ == "__main__":
    ut.main()