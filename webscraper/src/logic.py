from logic.webscraper import WebRetriever
from logic.parser import AlbertMenuParser

from bs4 import BeautifulSoup

if __name__ == "__main__":
    URL = "https://www.ah.nl/producten/9344/vlees"
    URL2 = "https://localhost:7061/Product"
    r = WebRetriever(URL2)
    albert = AlbertMenuParser(r)
    albert.parse()

    html = """
<div class="content dsa">First paragraph.</div>
<div class="content mano">Second paragraph.</div>
<p class="footer">Goodbye!</p>
"""
    soup = BeautifulSoup(html, 'html.parser')

# Find all <div> elements with the class "content"
    elements = soup.find_all('div', class_='content')
    for el in elements:
        print(el.text)

# Find just the first element with the class "content"
    first_element = soup.find(class_='content')