# Product Discovery Assistant

> **Status:** Beta 🚀

The **Product Discovery Assistant** is an end-to-end RAG (Retrieval-Augmented Generation) e-commerce assistant designed to transform how users find products. Unlike traditional keyword search, it understands abstract natural language queries (e.g., "bed for a small room") and provides intelligent, context-aware product recommendations with visual cards.

## ✨ Features

-   **AI-Powered Search:** Uses LLMs to "reason" about user queries and translate them into effective database searches.
-   **RAG Pipeline:** Combines vector search (Supabase pgvector) with LLM synthesis for accurate and explained results.
-   **Visual Recommendations:** Returns rich product cards with images, prices, and details, not just text.
-   **Modern Stack:** Built with React (Vite) for a responsive frontend and FastAPI for a high-performance backend.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

-   **Node.js** (v18 or higher)
-   **Python** (v3.10 or higher)
-   **Git**
-   **Supabase Account** (for Database & Vector Search)
-   **Google Gemini API Key** (for LLM & Embeddings)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone 'https://github.com/Ag-Utkarsh/product-discovery--assistant.git'
cd product-discovery--assistant
```

### 2. Backend Setup

Navigate to the backend directory and set up the Python environment.

```bash
cd backend
python -m venv venv

# Activate Virtual Environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install Dependencies
pip install -r requirement.txt
```

**Environment Configuration:**
Create a `.env` file in the `backend` directory:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
GOOGLE_API_KEY=your_google_api_key
```

### 3. Frontend Setup

Navigate to the frontend directory and install dependencies.

```bash
cd ../frontend
npm install
```

**Environment Configuration:**
Create a `.env` file in the `frontend` directory (optional if using default localhost):

```env
VITE_API_URL=http://localhost:8000
```

## 🏃 Usage

### Start the Backend Server

From the `backend` directory (with venv activated):

```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.
Documentation: `http://localhost:8000/docs`

### Start the Frontend Server

From the `frontend` directory:

```bash
npm run dev
```
The application will be available at `http://localhost:5173`.

## 📂 Project Structure

```text
product-discovery-assistant/
├── backend/                 # FastAPI Backend
│   ├── app/                 # Application Source
│   │   ├── main.py          # Entry Point
│   │   └── services/        # Business Logic (RAG, LLM, Product)
│   ├── tests/               # Unit Tests
│   └── requirements.txt     # Python Dependencies
├── frontend/                # React Frontend
│   ├── src/                 # Source Code
│   │   ├── components/      # Reusable Components
│   │   └── pages/           # Page Views
│   └── package.json         # Node Dependencies
└── docs/                    # Detailed Documentation
    ├── backend/             # Backend Specs & Architecture
    └── frontend/            # Frontend Architecture
```

## 🧪 Testing

### Backend
Run unit tests using pytest:

```bash
cd backend
pytest
```

## 📚 Documentation

For more detailed information about the system architecture and components, please refer to the following documents:

### Backend
- **[API Specification](docs/backend/api-spec.md):** Detailed list of API endpoints, request/response formats, and data models.
- **[Architecture Overview](docs/backend/architecture.md):** High-level design, data flow, and technology stack.
- **[Model Pipeline (RAG)](docs/backend/model-pipeline.md):** Explanation of the Retrieval-Augmented Generation pipeline, including query expansion and vector search.

### Frontend
- **[Component Map](docs/frontend/component-map.md):** Overview of the React component structure and hierarchy.
- **[State Management](docs/frontend/state-management.md):** Details on how state is handled within the application.

## 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.
