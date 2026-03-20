from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.documents import Document
import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_documents(data_path="data/", file_path=None):
    documents = []

    files_to_process = []
    if file_path:
        files_to_process.append(file_path)
    else:
        for f in os.listdir(data_path):
            files_to_process.append(os.path.join(data_path, f))

    for path in files_to_process:
        file = os.path.basename(path)

        if file.lower().endswith(".txt"):
            loader = TextLoader(path)
            documents.extend(loader.load())

        elif file.lower().endswith(".pdf"):
            try:
                loader = PyPDFLoader(path)
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading PDF {file}: {e}")

        elif file.lower().endswith((".png", ".jpg", ".jpeg")):
            try:
                img = PIL.Image.open(path)
                model = genai.GenerativeModel("gemini-2.5-flash")
                prompt = "Please provide a clear and conversational description of this image. Focus only on what is actually present in the image (e.g., objects, text, colors, people, scenery). Do not list things that are missing. The goal is to concisely explain what the image shows so it can be easily understood."
                response = model.generate_content([prompt, img])
                
                doc = Document(
                    page_content=f"Image Description for {file}:\n{response.text}",
                    metadata={"source": path}
                )
                documents.append(doc)
            except Exception as e:
                print(f"Error processing image {file}: {e}")

        else:
            continue

    return documents