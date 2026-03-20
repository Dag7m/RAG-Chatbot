# 🚀 RAG Chatbot System (Retrieval-Augmented Generation)

A full-stack **Retrieval-Augmented Generation (RAG)** system built on FastAPI and React. It acts as an intelligent, context-aware chatbot using custom uploaded documents. It flawlessly combines semantic text vectorization, multimodal vision ingestion, and Gemini LLMs to trace and cite accurate, grounded responses.

---

## 📌 Overview

This project implements an **end-to-end RAG pipeline**:

**Ingestion Pipeline**
→ Load documents (`.txt`, `.pdf`, `.png`, `.jpg`). Visual data is ingested via Gemini Vision textualization.
→ Split into semantic chunks
→ Embedding generation via HuggingFace `all-MiniLM-L6-v2`
→ Store sequentially into the Chroma vector database

**Retrieval Pipeline**
→ User questions the Chatbot
→ Query is embedded
→ Semantic search across local DB
→ Accurate context chunk retrieved
→ Conversational LLM response Generation via `Gemini-2.5-flash`

---

## ✨ Features

### 🔍 Core Features
* Seamless ingestion of **PDF, TXT, and Image files**.
* Native Semantic document search using embeddings.
* Conversational context-aware generation explicitly abstracting metadata from raw chunks.
* Fast, persistent vector database using Chroma.
* History-aware chat system dynamically stored locally.

### 💬 Chat Features
* "Da RAG" Ultra-modern frontend (Glassmorphism, SVG iconsets, subtle dynamic animations).
* Contextual "Thinking..." bouncing animated locators.
* Intelligent auto-scrolling capabilities to newest messages.

### 📂 File Upload Pipeline
* Upload text documents (`.txt`, `.pdf`) directly using the React "+" button.
* Automatically ingests **ONLY** the new file into the DB incrementally to prevent data duplication and ranking bloat!
* Explicitly states the uploaded target's filename immediately within the conversation.

### 👁️ Multimodal Integration
* Textualize any native picture (`.png`, `.jpg`, `.jpeg`).
* Images are explicitly described natively and intelligently by Gemini-2.5-Flash behind the scenes and embedded naturally into the semantic database!

### 📚 Source Transparency
* Pinpoints exact document chunks that informed the conversational answer.
* Highly boosts enterprise reliability and system explainability.

---

## 🏗️ Architecture Stack

### Backend Structure
* **Python FastApi Layer (`main.py`)**: Root logic mapping `upload`, `chat`, and `history` routing endpoints.
* **LangChain & ChromaDB Frameworks (`retrieval/` & `ingestion/`)**: Connects Vector Embeddings (`HuggingFace`) securely to the Local DB cache safely using explicit file management logic.

### Frontend
* **ReactJS**: React App configured at `/ui/src` with `axios` bindings.
* **Premium CSS Interface**: Located natively in `App.css`.

---

## 🛠️ Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd rag-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Make sure this installs `pypdf`, `pillow`, `google-generativeai`, and `huggingface-hub` successfully).*

### 4. Add Environment Variables
Create a `.env` file at the root containing your active AI API payload key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run API Backend
```bash
uvicorn main:app --reload
```
API runs smoothly on `http://127.0.0.1:8000`

### 6. Run React Frontend
```bash
cd ui
npm install
npm start
```

---

## 📡 Essential RAG Endpoints

### 🔹 `/upload`
* Pass `multipart/form-data` with files.
* Handles the incremental processing isolated for `.pdf`, `.txt`, `.jpg`.

### 🔹 `/chat`
* Request `{ "query" : "..." }`
* Yields the answer narrative safely alongside chunked references in `src`.

---

## 🚀 Key Iterated Design Decisions

- **Image Textualization over Multimodal Vectorizing:** Utilizing `Gemini` immediately during Ingestion provides an elegant, highly performant context integration for standard, computationally efficient text-based Retrieval (via ChromaDB).
- **Single-File Event Ingestion:** Explicitly bypassing mass-reloading `data/` prevents document scaling drift!
- **Sleek Aesthetic Integrations:** Enhancing the native frontend prevents dry functionality masking underlying complex vector workflows!

---

## 👨‍💻 Author
Developed and Iterated as part of RAG system design training.

