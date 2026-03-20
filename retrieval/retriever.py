from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_retriever():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    return retriever