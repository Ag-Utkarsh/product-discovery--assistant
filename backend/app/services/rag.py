import google.generativeai as genai
from app.core.config import GOOGLE_API_KEY
from app.core.db import supabase

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY must be set in .env file")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_embedding(text: str) -> list[float]:
    """
    Generates an embedding for the given text using Google's text-embedding-004 model.
    """
    try:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document",
            title="Product Embedding"
        )
        return result['embedding']
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return []

def search_products(query: str, match_threshold: float = 0.5, match_count: int = 5):
    """
    Searches for products using vector similarity.
    """
    # For query embedding, we use task_type="retrieval_query"
    try:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=query,
            task_type="retrieval_query"
        )
        query_embedding = result['embedding']
    except Exception as e:
        print(f"Error generating query embedding: {e}")
        return []

    if not query_embedding:
        return []
    
    try:
        response = supabase.rpc(
            'match_products',
            {
                'query_embedding': query_embedding,
                'match_threshold': match_threshold,
                'match_count': match_count
            }
        ).execute()
        return response.data
    except Exception as e:
        print(f"Error searching products: {e}")
        return []
