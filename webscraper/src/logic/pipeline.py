from .load import DataLoader
from .parser import Parser

class CollectionPipeline:

    def __init__(self, webscraper, loader):
        self.webscraper: Parser = webscraper
        self.data_loader: DataLoader = loader
        
    def execute(self):
        try:
            data = self.webscraper.parse()
            self.data_loader.load(data)
            return True
        except Exception:
            print("Failed data collection")
            return False
        
        