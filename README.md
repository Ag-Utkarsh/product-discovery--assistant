# Product Discovery Assistant

A RAG-powered e-commerce assistant that helps users find products using natural language queries. Built for the Neusearch AI Engineering Intern assignment.

## 🌟 Features

-   **Natural Language Search:** Users can ask for products using everyday language (e.g., "I need a dress for a summer wedding").
-   **RAG Pipeline:** Combines vector search (Supabase pgvector) with LLM generation (Google Gemini) to provide accurate and context-aware recommendations.
    -   **How it works:**
        1.  **User Query:** The user submits a natural language query.
        2.  **LLM (Query Expansion):** The query is processed by an LLM to generate synonyms and related search terms, improving search recall.
        3.  **RAG (Vector Search):** The expanded query is converted into a vector embedding.
        4.  **Database (Retrieval):** The embedding is used to query Supabase (pgvector) for semantically similar products.
        5.  **LLM (Response Synthesis):** The retrieved product data and the original query are sent to the LLM to generate a natural, helpful response.
        6.  **Response:** The final answer and product recommendations are presented to the user.
-   **Interactive Chat:** A conversational interface to refine searches and ask follow-up questions.
-   **Product Details:** View detailed product information including price, description, and features.
-   **Modern UI:** A responsive and aesthetically pleasing React frontend inspired by Hunnit.com.

## 🚀 Tech Stack

-   **Frontend:** React, Vite, Tailwind CSS, Lucide React
-   **Backend:** Python, FastAPI
-   **Database:** Supabase (PostgreSQL + pgvector)
-   **AI/LLM:** Google Gemini (Embeddings & Chat)
-   **Data Source:** Hunnit.com (Scraped)

## 🏗️ Architecture

1.  **Data Collection:** Product data is scraped from Hunnit.com and structured into JSON.
2.  **Ingestion Pipeline:**
    -   Reads structured JSON data.
    -   Generates vector embeddings for product descriptions and features using `models/text-embedding-004`.
    -   Stores product metadata and embeddings in Supabase.
3.  **Backend API:**
    -   FastAPI server providing endpoints for product listing and details.
    -   Connects to Supabase for data retrieval.
4.  **Frontend UI:**
    -   Modern, responsive React application.
    -   Features a clean grid layout, bold typography, and optimized product cards.

## 🛠️ Setup & Installation

### Prerequisites

-   Python 3.8+
-   Node.js & npm
-   Supabase Account
-   Google Cloud API Key (for Gemini)

### 1. Clone the Repository

```bash
git clone https://github.com/Ag-Utkarsh/Product-Discovery-Assistant.git
cd "Product Discovery Assistant"
```

### 2. Backend Setup

1.  **Create a virtual environment:**
    ```bash
    cd backend
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**
    Create a `.env` file in the `backend` directory:
    ```env
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    GOOGLE_API_KEY=your_google_api_key
    ```

4.  **Database Setup (Supabase):**
    Run the SQL script located at `backend/app/core/setup.sql` in your Supabase SQL Editor. This will:
    -   Enable the `vector` extension.
    -   Create `products` and `product_embeddings` tables.
    -   Create the `match_products` function for similarity search.

5.  **Data Ingestion:**
    Run the ingestion script to populate the database:
    ```bash
    python -m app.services.ingest_data
    ```

6.  **Run the Server:**
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    The API will be available at `http://localhost:8000`.

### 3. Frontend Setup

1.  **Navigate to frontend directory:**
    ```bash
    cd ../frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the Development Server:**
    ```bash
    npm run dev
    ```
    The UI will be available at `http://localhost:5173`.

## � API Reference

### Products

-   **List Products**
    -   `GET /products?limit=20&offset=0`
    -   Returns a paginated list of products.

-   **Get Product**
    -   `GET /products/{product_id}`
    -   Returns details for a specific product.

### Chat

-   **Chat with Assistant**
    -   `POST /chat`
    -   **Body:** `{ "query": "Find me a blue shirt" }`
    -   **Response:**
        ```json
        {
          "response": "Here are some blue shirts I found...",
          "products": [ ... ]
        }
        ```

## �📂 Project Structure

```
Product Discovery Assistant/
├── backend/
│   ├── app/
│   │   ├── core/          # Config & DB setup
│   │   ├── services/      # Ingestion & RAG logic
│   │   └── main.py        # FastAPI endpoints
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page views
│   │   └── App.jsx        # Main application component
│   └── package.json
└── README.md
```
