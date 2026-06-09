from logic.webscraper import WebRetriever
from logic.parser import AlbertMenuParser

if __name__ == "__main__":
    URL = "https://www.ah.nl/producten/9344/vlees"
    URL2 = "https://localhost:7061/counter"
    r = WebRetriever(URL)
    albert = AlbertMenuParser(r)
    albert.parse()