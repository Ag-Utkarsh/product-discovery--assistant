import json
import os
import sys

# Add the backend directory to sys.path to allow imports from app
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from app.core.db import supabase
from app.services.rag import generate_embedding

def ingest_data():
    """
    Reads product data from JSON and ingests it into Supabase.
    """
    json_path = os.path.join(os.path.dirname(__file__), 'hunnit_products.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            products = json.load(f)
            
        print(f"Read {len(products)} products from {json_path}")
        
        for product in products:
            print(f"Processing: {product['title']}")
            
            # 1. Insert into products table
            # Schema: id, sku_id, title, price, description, image_url, source_url, features (jsonb), category
            
            product_data = {
                "sku_id": f"HUNNIT-{product['id']}", # Generate a SKU
                "title": product['title'],
                "price": product['price'],
                "image_url": product['image_url'],
                "source_url": "https://hunnit.com/collections/all", # Hardcoded source
                "features": {
                    "attributes": product.get('features', []),
                    "colors": product.get('colors', []),
                    "rating": product.get('rating')
                },
                "category": product.get('category', 'Uncategorized')
            }
            
            # Upsert product
            response = supabase.table('products').upsert(product_data, on_conflict='sku_id').execute()
            
            if not response.data:
                print(f"Failed to upsert product: {product['title']}")
                continue
                
            product_id = response.data[0]['id']
            
            # 2. Generate Embedding
            # Create a rich text representation for embedding
            text_to_embed = f"{product['title']} {', '.join(product.get('features', []))} {product.get('category', '')}"
            embedding = generate_embedding(text_to_embed)
            
            if not embedding:
                print(f"Failed to generate embedding for: {product['title']}")
                continue
                
            # 3. Insert into product_embeddings table
            embedding_data = {
                "product_id": product_id,
                "chunk_content": text_to_embed,
                "embedding": embedding
            }
            
            supabase.table('product_embeddings').insert(embedding_data).execute()
            
        print("Data ingestion complete!")
            
    except FileNotFoundError:
        print(f"Error: File not found at {json_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ingest_data()
