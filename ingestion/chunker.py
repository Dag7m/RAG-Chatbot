from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

def chunk_documents(documents):
    # Initialize the same embeddings used globally in the project
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Establish a semantic chunker splitting by percentile gaps in vector meaning
    splitter = SemanticChunker(embedding_model, breakpoint_threshold_type="percentile")

    try:
        chunks = splitter.split_documents(documents)
        if not chunks:
            return documents
    except Exception as e:
        print(f"SemanticChunker bypassed: document too short or incompatible ({e}). Using full docs.")
        return documents

    return chunks