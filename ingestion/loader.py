from langchain_community.document_loaders import TextLoader
import os

def load_documents(data_path="data/"):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            documents.extend(loader.load())

    return documents