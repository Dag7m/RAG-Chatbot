from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from utils.memory import load_history
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
    answer = ask_question(request.query)
    return {"response": answer}


# File upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Re-run ingestion after upload
    run_ingestion()

    return {"message": "File uploaded and processed successfully"}

@app.get("/history")
async def get_history():
    history = load_history()
    return {"history": history}