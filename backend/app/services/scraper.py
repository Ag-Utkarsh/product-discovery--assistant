import requests
from bs4 import BeautifulSoup
import json
import time
import re

BASE_URL = "https://hunnit.com"
COLLECTION_URL = "https://hunnit.com/collections/all"

def get_soup(url):
    """Fetches the URL and returns a BeautifulSoup object."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def clean_text(text):
    """Cleans whitespace from text."""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def parse_price(text):
    """Extracts the first integer price from a string."""
    if not text:
        return 0
    # Remove non-numeric characters except for potential delimiters if needed, 
    # but here we just want the number.
    # Strategy: Find digits.
    clean = re.sub(r'[^\d]', '', text)
    return int(clean) if clean else 0

def extract_price(soup):
    """Extracts the selling price of the product."""
    # Priority 1: Explicit current price class
    price_tag = soup.select_one(".current-price")
    if price_tag:
        return parse_price(price_tag.get_text())
    
    # Priority 2: Sale price class
    price_tag = soup.select_one(".price-item--sale")
    if price_tag:
        return parse_price(price_tag.get_text())
    
    # Priority 3: Fallback to general price container, excluding 'was-price'
    price_container = soup.select_one(".price, .product-price, #ProductPrice")
    if price_container:
        # Remove known non-selling price elements
        for bad in price_container.select(".was-price, .price-item--regular, .compare-price"):
            bad.decompose()
        
        text = price_container.get_text()
        # Look for "Rs. 1,234" pattern
        matches = re.findall(r'Rs\.\s*[\d,]+', text)
        if matches:
            return parse_price(matches[0])
            
    return 0

def extract_description_and_features(soup):
    """Extracts description and features from the product page."""
    description = "N/A"
    features = []

    # Strategy: Find "Why you’ll love this?" header
    desc_header = soup.find(string=re.compile(r"Why you’ll love this\?", re.IGNORECASE))
    if desc_header:
        container = desc_header.find_parent("div") or desc_header.find_parent("section")
        if container:
            full_text = container.get_text(separator="\n")
            parts = full_text.split("Why you’ll love this?")
            if len(parts) > 1:
                description = clean_text(parts[1].split("Product Features")[0])

    # Features
    feat_header = soup.find(string=re.compile(r"Product Features", re.IGNORECASE))
    if feat_header:
        container = feat_header.find_parent("div") or feat_header.find_parent("section")
        if container:
            full_text = container.get_text(separator="\n")
            parts = full_text.split("Product Features")
            if len(parts) > 1:
                feature_text = parts[1].split("Fabric Features")[0]
                for f in feature_text.split('\n'):
                    clean_f = clean_text(f)
                    if clean_f and len(clean_f) > 3:
                        features.append(clean_f)

    # Fallback for description
    if description == "N/A" or not description:
        meta_desc = soup.select_one("meta[name='description']")
        if meta_desc:
            description = meta_desc['content']

    return description, features

def scrape_product_details(product_url):
    """Scrapes details for a single product."""
    soup = get_soup(product_url)
    if not soup:
        return None

    product = {
        'url': product_url,
        'category': "Uncategorized" # Default
    }

    # Title
    title_tag = soup.select_one("h1.product-title, h1.title, .product_title")
    product['title'] = clean_text(title_tag.get_text()) if title_tag else "N/A"

    # Price
    product['price'] = extract_price(soup)

    # Description & Features
    desc, feats = extract_description_and_features(soup)
    product['description'] = desc
    product['features'] = feats

    # Image URL
    image_tag = soup.select_one("meta[property='og:image']")
    if image_tag:
        product['image_url'] = image_tag['content']
    else:
        img_tag = soup.select_one(".product-gallery img, .product-photo-container img")
        product['image_url'] = "https:" + img_tag['src'] if img_tag else "N/A"

    # Category (Breadcrumbs)
    breadcrumbs = soup.select(".breadcrumb a, .breadcrumbs a, nav[aria-label='breadcrumbs'] a")
    if breadcrumbs and len(breadcrumbs) > 1:
        cat_cand = clean_text(breadcrumbs[1].get_text())
        if cat_cand.lower() != "home":
            product['category'] = cat_cand

    return product

def scrape_hunnit_products():
    """Main function to scrape products."""
    print(f"Fetching product list from {COLLECTION_URL}...")
    soup = get_soup(COLLECTION_URL)
    if not soup:
        print("Failed to load collection page.")
        return

    # Find unique product links
    product_links = set()
    for a in soup.select("a[href*='/products/']"):
        href = a['href']
        if "/products/" in href:
            full_url = BASE_URL + href if href.startswith("/") else href
            full_url = full_url.split('?')[0]
            product_links.add(full_url)

    print(f"Found {len(product_links)} unique product links.")

    products = []
    target_count = 25

    for i, link in enumerate(product_links):
        if i >= target_count:
            break
        
        print(f"Scraping ({i + 1}/{target_count}): {link}")
        product_data = scrape_product_details(link)
        if product_data:
            products.append(product_data)
            time.sleep(1) 

    # Save to JSON
    output_file = "products.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)
    
    print(f"Scraping complete. Saved {len(products)} products to {output_file}.")

if __name__ == "__main__":
    scrape_hunnit_products()
