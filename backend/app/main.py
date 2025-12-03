from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import supabase
from pydantic import BaseModel
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Product Discovery Assistant")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    id: str
    sku_id: str
    title: str
    price: int
    description: Optional[str] = None
    image_url: Optional[str] = None
    source_url: Optional[str] = None
    features: Optional[dict] = None
    category: Optional[str] = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to Product Discovery Assistant API"}

@app.get("/products", response_model=List[Product])
async def get_products(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    List products with pagination.
    """
    try:
        response = supabase.table("products").select("*").range(offset, offset + limit - 1).execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    """
    Get a single product by ID.
    """
    try:
        response = supabase.table("products").select("*").eq("id", product_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Product not found")
        return response.data[0]
    except Exception as e:
        logger.error(f"Error fetching product {product_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
