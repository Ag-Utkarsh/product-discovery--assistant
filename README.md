# Product Discovery Assistant

A RAG-powered e-commerce assistant that helps users find products using natural language queries. Built for the Neusearch AI Engineering Intern assignment.

## 🚀 Tech Stack

- **Frontend:** React, Vite, Tailwind CSS
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
3.  **Backend API:**
    - FastAPI server providing endpoints for product listing and details.
    - Connects to Supabase for data retrieval.
4.  **Frontend UI:**
    - Modern, responsive React application.
    - Design inspired by Hunnit.com.
    - Features a clean grid layout, bold typography, and optimized product cards.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.8+
- Node.js & npm
- Supabase Account
- Google Cloud API Key (for Gemini)

### 1. Clone & Install Dependencies

```bash
# Clone the repository
git clone 'https://github.com/Ag-Utkarsh/Product-Discovery-Assistant.git'
cd 'Product Discovery Assistant'
```

#### Backend Setup
```bash
# Create and activate virtual environment
python -m venv backend/venv
# Windows:
backend\venv\Scripts\activate
# Mac/Linux:
source backend/venv/bin/activate

# Install dependencies
pip install -r backend/requirement.txt
```

#### Frontend Setup
```bash
cd frontend
npm install
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

## 🏃‍♂️ Running the Application

### Start the Backend Server
```bash
# From the root directory
cd backend
# Ensure venv is active
uvicorn app.main:app --reload --port 8000
```
The API will be available at `http://localhost:8000`.

### Start the Frontend Server
```bash
# From the root directory
cd frontend
npm run dev
```
The UI will be available at `http://localhost:5173`.

## 📂 Project Structure

```
Product Discovery Assistant/
├── backend/
│   ├── app/
│   │   ├── core/          # Config & DB setup
│   │   ├── services/      # Ingestion & RAG logic
│   │   └── main.py        # FastAPI endpoints
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/    # Reusable UI components (ProductCard)
│   │   ├── pages/         # Page views (Home, ProductDetail)
│   │   └── ...
│   └── ...
└── ...
```
