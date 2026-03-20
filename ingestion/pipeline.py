from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from ingestion.loader import load_documents
from ingestion.chunker import chunk_documents

def run_ingestion(file_path=None):
    documents = load_documents(file_path=file_path)
    if not documents:
        print(f"Skipping ingestion: no documents found for {file_path}")
        return
    chunks = chunk_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="chroma_db"
    )

    # vectordb.persist()

    print("✅ Ingestion completed!")