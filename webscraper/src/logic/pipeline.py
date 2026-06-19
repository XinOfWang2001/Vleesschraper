from .load import DataLoader
from .parser import Parser

class CollectionPipeline:

    def __init__(self, webscraper: Parser, loader: DataLoader):
        self.webscraper: Parser = webscraper
        self.data_loader: DataLoader = loader
        
    def execute(self):
        try:
            data = self.webscraper.parse()
            self.data_loader.load(data)
            return True
        except Exception as ex:
            raise ex
        
        