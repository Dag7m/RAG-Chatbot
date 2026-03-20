from langchain_text_splitters import NLTKTextSplitter

def chunk_documents(documents):
    splitter = NLTKTextSplitter(chunk_size=500)

    chunks = splitter.split_documents(documents)

    return chunks