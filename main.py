from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from utils.memory import load_history, add_to_history
from pydantic import BaseModel
from retrieval.chat import ask_question
from ingestion.pipeline import run_ingestion

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    answer, sources = ask_question(request.query)

    return {
        "response": answer,
        "sources": sources
    }

# File upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    run_ingestion(file_path=file_path)

    # ✅ Add upload event to history
    add_to_history(
        f"I uploaded a file: {file.filename}",
        f"File '{file.filename}' processed and added to the knowledge base."
    )

    return {"message": f"File '{file.filename}' uploaded and processed successfully", "filename": file.filename}

@app.get("/history")
async def get_history():
    history = load_history()
    return {"history": history}