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

---

## 🏗️ Architecture Stack & System Components

### Execution Flow
- `ui/src/App.js`: The front-facing React app handling user inputs, rapid file uploads, and tracking visual chat loops dynamically via glassmorphic aesthetics.
- `main.py`: The entry hub. Contains API routing (`/chat`, `/upload`, `/history`). Handlers orchestrate the pipelines below incrementally.
- `ingestion/loader.py`: Extracts unstructured text from raw files (`.txt`, `.pdf`, `.png`, `.jpg`). Multimodal image data is instantly narrated natively by Gemini Vision here.
- `ingestion/chunker.py`: Implements advanced LangChain `SemanticChunker` logic. Replaces rudimentary sentence splitting with ML-driven embedding gap calculations!
- `ingestion/pipeline.py`: Embeds the semantic chunks into numerical vectors and commits them to the local Vector Database incrementally.
- `retrieval/retriever.py`: Takes user queries, transforms them into comparable vectors, and extracts highly-correlated, previously archived chunks from the database!
- `retrieval/generator.py`: Feeds the retrieved chunks and the user's prompt directly to `Gemini-2.5-flash`. The prompt has been refined to enforce concise, conversational RAG narration while hiding metadata.
- `utils/memory.py`: Tracks raw chat history objects seamlessly within a simple local `.json` file (`chat_history.json`).

---

## 🧠 Core RAG Concepts Addressed

### 1. Data Persistence (Chroma DB)
Data persists seamlessly through restarts because the backend operates heavily on Local Disk States!
When a file is ingested, `Chroma` writes the spatial embeddings to the `chroma_db/` SQLite-based directory.
When you close your app and kill the backend, the `chroma_db/` folder remains preserved safely. Upon restarting, `retriever.py` initializes by explicitly pointing at `persist_directory="chroma_db"`, ensuring everything ingested previously remains exactly accessible!

### 2. The Multimodal Approach (Textualization)
True native Multimodal RAG relies on *Multimodal Embeddings* (e.g., CLIP by OpenAI) which convert image pixels directly into vectors. However, image-heavy vectors increase compute load significantly and make similarity matching computationally heavy for local dev. 
Because this engine specifically utilizes `ChromaDB` alongside HuggingFace `all-MiniLM-L6-v2` semantic models (which expect text vectors), treating `Gemini 2.5 Flash` as an **Ingestion Oracle** to convert deep visual representations into verbose native text descriptions handles edge cases brilliantly. This achieves full multimodality (Textualization) cleanly!

### 3. Source Accountability
A large piece of what makes our RAG so powerful is explainability.
When asking a question:
1. The Retriever queries the database and grabs `k=3` matching Documents.
2. The Generator logically wraps these 3 documents inside the invisible `system prompt` sent to Gemini.
3. Simultaneously, the framework aggregates the raw strings that were matched into a JSON array boundary. 
4. This list is passed straight back to the React UI `App.js`!
5. `App.js` gracefully enumerates these verbatim strings explicitly inside the **Sources:** interface panel!

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

