# Hunnit.com Product Scraper

The scraper is a standalone Python script designed to extract product data from [Hunnit.com](https://hunnit.com/collections/all) for the Product Discovery Assistant.

## Purpose

To populate the product database with real-world fashion items, including rich metadata like descriptions, features, and images, which are essential for the RAG pipeline to function effectively.

## Usage

The scraper is located in `backend/app/services/scraper.py`.

### Running the Scraper

From the `backend` directory with your virtual environment activated:

```bash
python app/services/scraper.py
```

### Output

The script generates a `products.json` file in the `backend` directory containing a list of product objects.

**Sample Output:**

```json
[
    {
        "url": "https://hunnit.com/products/example-product",
        "title": "Example Product Title",
        "price": 1299,
        "description": "Full product description text...",
        "features": [
            "Feature 1",
            "Feature 2"
        ],
        "image_url": "https://hunnit.com/cdn/shop/...",
        "category": "Uncategorized"
    }
]
```

## Implementation Details

### Key Functions

-   **`scrape_hunnit_products()`**: Main entry point. Fetches the collection page, extracts product links, and iterates through them.
-   **`scrape_product_details(url)`**: Orchestrates the extraction for a single product page.
-   **`extract_price(soup)`**: Robust logic to find the selling price. Prioritizes `.current-price` and `.price-item--sale` classes to ensure discounted prices are captured correctly as integers.
-   **`extract_description_and_features(soup)`**: Uses regex to locate "Why you’ll love this?" and "Product Features" sections to parse unstructured text into clean descriptions and lists.

### Dependencies

-   `requests`: For HTTP requests.
-   `beautifulsoup4`: For HTML parsing.
