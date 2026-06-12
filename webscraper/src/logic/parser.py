from .webscraper import WebRetriever
from bs4 import BeautifulSoup
from datetime import datetime
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
        collection_meat = []
        # Might
        bs4 = BeautifulSoup(web_page.html_content, "html.parser")
        
        # Eerst find all zoeken
        products = bs4.find_all("div", class_="product-card-container_horizontalContainer__Olj6l")
        # Start mapping product information to entity file.
        while(len(products) > 0):
            product = products.pop()
            # Dan find methode gebruiken
            # Seems like a working solution. Now to make it more robust and compatible with Blazor
            title = product.find("p", class_= "typography_typography__1WfcP")
            price = product.find("p", class_="product-card-current-price_root__7_1ri")
            weight = product.find("p", class_="product-dcad-current-weight")
            meat = MeatProduct(date_time=datetime.now(), 
                        supermarket="AH", 
                        full_title=title, 
                        capitilized_title=title.get_text().capitalize(),
                        current_price=price,
                        weight=weight)
            collection_meat.append(meat)
        # Decide if the implementation needs to be split to specific use cases or not.
        return collection_meat