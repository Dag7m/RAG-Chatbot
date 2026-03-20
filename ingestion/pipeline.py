from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from ingestion.loader import load_documents
from ingestion.chunker import chunk_documents

def run_ingestion():
    documents = load_documents()
    chunks = chunk_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    # vectordb.persist()

    print("✅ Ingestion completed!")