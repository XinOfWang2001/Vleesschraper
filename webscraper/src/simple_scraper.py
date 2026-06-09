"""
Albert Heijn Web Scraper
Scrapes meat products from Albert Heijn website
"""
import requests
from bs4 import BeautifulSoup
import json
import re
import time
from datetime import datetime

# Configuration
ALBERT_HEIJN_URL = "https://www.ah.nl/producten/9344/vlees"
OUTPUT_FILE = "scraped_ah_products.json"

# Headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def scrape_website(url):
    """
    Scrape Albert Heijn website for meat products
    
    Args:
        url: The URL of the Albert Heijn products page
        
    Returns:
        dict: Scraped data with products
    """
    try:
        print(f"Fetching {url}...")
        print("Please wait, this may take a moment...\n")
        
        # Fetch the webpage with proper headers
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data
        data = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "title": soup.title.string if soup.title else "Albert Heijn - Vlees",
            "products": []
        }
        
        # Find all product card links with the specific class structure
        product_links = soup.find_all('a', class_=lambda x: x and 'product-card-container_linkContainer' in x)
        
        print(f"Found {len(product_links)} product links\n")
        
        for idx, link in enumerate(product_links, 1):
            product_data = extract_ah_product_data(link)
            if product_data:
                data["products"].append(product_data)
                print(f"{idx}. {product_data.get('name', 'Unknown')} - {product_data.get('price', 'N/A')}")
        
        print(f"\n✓ Successfully scraped {url}")
        print(f"  - Total products found: {len(data['products'])}")
        
        return data
        
    except requests.exceptions.ConnectionError:
        print(f"✗ Could not connect to {url}")
        return None
    except requests.exceptions.Timeout:
        print(f"✗ Request timeout. The server took too long to respond.")
        return None
    except Exception as e:
        print(f"✗ Error scraping {url}: {e}")
        return None


def extract_ah_product_data(link):
    """
    Extract product data from Albert Heijn product link
    
    Args:
        link: BeautifulSoup element containing product link
        
    Returns:
        dict: Product data or None
    """
    try:
        product = {}
        
        # Extract product URL
        href = link.get('href')
        if href:
            product['url'] = f"https://www.ah.nl{href}" if href.startswith('/') else href
        
        # Extract aria-label which contains: "Product Name, Nutri-Score X, Weight €Price, Extra info"
        aria_label = link.get('aria-label', '')
        if aria_label:
            product['raw_label'] = aria_label
            
            # Parse the aria-label
            # Example: "AH Rundergehakt, Nutri-Score C, 500 gram €5.55, Prijsfavoriet"
            parts = [p.strip() for p in aria_label.split(',')]
            
            if len(parts) > 0:
                product['name'] = parts[0]
            
            if len(parts) > 1:
                product['nutri_score'] = parts[1]
            
            # Extract weight and price from the string
            price_match = re.search(r'€[\d,\.]+', aria_label)
            if price_match:
                product['price'] = price_match.group()
            
            # Try to find weight
            weight_match = re.search(r'(\d+[\s\.]?\d*)\s*(gram|kg|ml|l)', aria_label, re.IGNORECASE)
            if weight_match:
                product['weight'] = f"{weight_match.group(1)} {weight_match.group(2)}"
            
            # Check for special labels
            if 'Prijsfavoriet' in aria_label:
                product['price_favorite'] = True
            if 'Biologisch' in aria_label or 'Bio' in aria_label:
                product['organic'] = True
        
        # Try to extract image from link or its parent
        img = link.find('img')
        if img:
            img_src = img.get('src')
            if img_src:
                product['image_url'] = img_src
            img_alt = img.get('alt')
            if img_alt:
                product['image_alt'] = img_alt
        
        # Return product only if we found name and price
        if 'name' in product and 'price' in product:
            return product
        return None
        
    except Exception as e:
        print(f"  Warning: Could not extract product data: {e}")
        return None


def save_data(data, filename):
    """Save scraped data to JSON file"""
    if data:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Data saved to {filename}")
        return True
    return False


if __name__ == "__main__":
    print("=" * 70)
    print("Albert Heijn Meat Products Scraper")
    print("=" * 70)
    print()
    
    # Scrape the Albert Heijn meat products page
    scraped_data = scrape_website(ALBERT_HEIJN_URL)
    
    if scraped_data and scraped_data['products']:
        save_data(scraped_data, OUTPUT_FILE)
        
        # Print detailed summary
        print("\n" + "=" * 70)
        print("Product Details:")
        print("=" * 70)
        
        for i, product in enumerate(scraped_data['products'], 1):
            print(f"\n[Product {i}]")
            print(f"  Name: {product.get('name', 'N/A')}")
            print(f"  Price: {product.get('price', 'N/A')}")
            if product.get('weight'):
                print(f"  Weight: {product.get('weight')}")
            if product.get('nutri_score'):
                print(f"  Nutri-Score: {product.get('nutri_score')}")
            if product.get('price_favorite'):
                print(f"  ⭐ Prijsfavoriet (Price Favorite)")
            if product.get('organic'):
                print(f"  🌿 Biologisch (Organic)")
            if product.get('url'):
                print(f"  URL: {product.get('url')}")
        
        print("\n" + "=" * 70)
        print(f"✓ Total products scraped: {len(scraped_data['products'])}")
        print(f"✓ Data saved to: {OUTPUT_FILE}")
        print("=" * 70)
    else:
        print("\n✗ No products found. Please check:")
        print("  - Is the website accessible?")
        print("  - Has the website structure changed?")
        print("  - Try running again or check the website manually.")
