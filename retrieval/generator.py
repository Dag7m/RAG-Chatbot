import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(query, context):
    prompt = f"""
You are a helpful assistant.

Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text