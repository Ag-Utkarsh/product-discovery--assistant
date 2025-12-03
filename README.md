# Product Discovery Assistant

A RAG-powered e-commerce assistant that helps users find products using natural language queries. Built for the Neusearch AI Engineering Intern assignment.

## 🚀 Tech Stack

- **Backend:** Python, FastAPI
- **Database:** Supabase (PostgreSQL + pgvector)
- **AI/LLM:** Google Gemini (Embeddings & Chat)
- **Data Source:** Hunnit.com (Scraped)

## 🏗️ Architecture

1.  **Data Collection:** Product data is scraped from Hunnit.com and structured into JSON.
2.  **Ingestion Pipeline:**
    - Reads structured JSON data.
    - Generates vector embeddings for product descriptions and features using `models/text-embedding-004`.
    - Stores product metadata and embeddings in Supabase.
3.  **RAG Pipeline (In Progress):**
    - Semantic search using vector similarity (`<=>` operator).
    - LLM-based query expansion and response generation.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- Supabase Account
- Google Cloud API Key (for Gemini)

### 1. Clone & Install Dependencies

```bash
# Clone the repository
git clone <repo-url>
cd "Product Discovery Assistant"

# Create and activate virtual environment
python -m venv backend/venv
# Windows:
backend\venv\Scripts\activate
# Mac/Linux:
source backend/venv/bin/activate

# Install dependencies
pip install -r backend/requirement.txt
```

### 2. Environment Configuration

Create a `.env` file in the `backend/` directory:

```ini
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
GOOGLE_API_KEY=your_google_api_key
```

### 3. Database Setup (Supabase)

Run the SQL script located at `backend/app/core/setup.sql` in your Supabase SQL Editor. This will:
- Enable the `vector` extension.
- Create `products` and `product_embeddings` tables.
- Create the `match_products` function for similarity search.

### 4. Data Ingestion

Run the ingestion script to populate the database:

```bash
python backend/app/services/ingest_data.py
```

## 📂 Project Structure

```
backend/
├── app/
│   ├── core/
│   │   ├── config.py      # Environment config
│   │   ├── db.py          # Supabase client
│   │   └── setup.sql      # Database schema
│   ├── services/
│   │   ├── ingest_data.py # Data ingestion script
│   │   ├── rag.py         # Vector search logic
│   │   ├── llm.py         # LLM integration (Todo)
│   │   └── hunnit_products.json # Scraped data
│   └── main.py            # FastAPI entry point
├── requirement.txt
└── venv/
```

## ✅ Progress Log

- [Done] **Data Scraping:** Scraped 29 products from Hunnit.com.
- [Done] **Data Parsing:** Converted raw text to structured JSON.
- [Done] **Database Design:** Schema designed for RAG (using `jsonb` for features).
- [Done] **Vector Search Setup:** Configured `pgvector` with 768 dimensions for Gemini embeddings.
- [Done] **Data Ingestion:** Successfully uploaded products and embeddings to Supabase.
- [ ] **API Development:** FastAPI endpoints for Chat and Product Listing.
- [ ] **Frontend:** React UI (Next Steps).
