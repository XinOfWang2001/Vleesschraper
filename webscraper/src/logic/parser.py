from .webscraper import WebRetriever
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from domain.meat_product import MeatProduct


# Specific implementation per supermarket.
# - AH
# - Jumbo
# - Dirk

# All should be to a set format


class Parser(ABC):

    @abstractmethod
    def parse(self) -> list[MeatProduct]:
        pass

URL = "https://www.ah.nl/producten/9344/vlees"

# Specific implementation for menu products of the AH
class AlbertMenuParser(Parser):
    retriever: WebRetriever

    def __init__(self, web_retriever: WebRetriever):
        self.retriever = web_retriever
        

    def parse(self):
        web_page = self.retriever.scrape_site()
        # Might
        bs4 = BeautifulSoup(web_page.html_content, "html.parser")

        products = bs4.find_all("a", class_=lambda x: x and 'product-card-container_linkContainer' in x)
        for product in products:
            print(product)

        # Decide if the implementation needs to be split to specific use cases or not.
        return super().parse()