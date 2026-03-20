import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_answer(query, context):
    prompt = f"""
You are an intelligent, friendly AI assistant.
Your goal is to answer the user's question directly and conversationally using ONLY the provided context.
When discussing files or images, talk about them naturally based on the provided descriptions. Do NOT leak raw metadata formats, rigid descriptions, or internal system formatting.

Context:
{context}

Question:
{query}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text