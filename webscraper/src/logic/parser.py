from abc import ABC, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup

from ..domain import MeatProduct
from .webscraper import WebRetriever

# Specific implementation per supermarket.
# - AH
# - Jumbo
# - Dirk

# All should be to a set format


class Parser(ABC):

    @abstractmethod
    def parse(self) -> list[MeatProduct]:
        pass

# Specific implementation for menu products of the AH
class AlbertMenuParser(Parser):
    retriever: WebRetriever
    mark_grocery_store = "AH"

    def __init__(self, web_retriever: WebRetriever):
        self.retriever = web_retriever
        

    def parse(self):
        web_page = self.retriever.scrape_site()
        bs4 = BeautifulSoup(web_page.html_content, "html.parser")
        # Eerst find all zoeken
        products = bs4.find_all("div", class_="product-card-container_horizontalContainer__Olj6l")
        # Decide if the implementation needs to be split to specific use cases or not.
        return self.further_parse(products, web_page.date_time, [])
    
    def further_parse(self, elements: list, current_date: datetime, collection: list[MeatProduct]):
        # Stop condition.
        if(len(elements) == 0):
            return collection
        product = elements.pop()
        condition =  lambda text: "typography_typography" in text
        current_price_condition =  lambda text: "product-card-current-price_root" in text
        original_price_condition =  lambda text: "original-price_root" in text
        product_weight_condition =  lambda text: "product-card-content_priceDescription" in text
        # Searches information within markup.
        title: str = product.find("p", class_=condition).get_text(strip=True)
        
        current_price: str = product.find("p", class_=current_price_condition).get_text()
        old_price = product.find("p", class_=original_price_condition)
        weight: str = product.find("p", class_=product_weight_condition).get_text(separator=" ", strip=True)
        # Specific logic to parse the information is necessary for discount checking or weights parsing.
        old_price = self._parse_discounts(old_price, current_price)
        weight_float: int = self._parse_weight(weight)
        # Create entity
        meat = MeatProduct(date_time=current_date, supermarket=self.mark_grocery_store, 
                    full_title=title, capitilized_title=title.capitalize(),
                    current_price= float(current_price), normal_price= float(old_price),
                    weight=weight_float)
        collection.append(meat)
        return self.further_parse(elements, current_date, collection)
    
    def _parse_discounts(self, old, current):
        # Check if old price exists, just to detect if a discount is present.
        if(old is not None):
            # Assign regular price if no discount is applied
            return old.get_text()
        return current
    
    def _partial_match(self, condition, text) -> str:
        return condition in text
    
    def _parse_weight(self, weight: str) -> int:
        weight = weight.replace("ca. ", "")
        splits = weight.split(" ")[0]
        try:
            return int(splits)
        except Exception:
            return 0
