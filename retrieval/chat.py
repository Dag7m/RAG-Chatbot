from retrieval.retriever import get_retriever
from retrieval.generator import generate_answer
from utils.memory import add_to_history, get_history_text

def ask_question(query):
    retriever = get_retriever()  # 🔥 ALWAYS refresh

    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    history_text = get_history_text()

    full_context = f"""
Chat History:
{history_text}

Retrieved Context:
{context}
"""

    answer = generate_answer(query, full_context)

    add_to_history(query, answer)

    sources = [doc.page_content for doc in docs]

    return answer, sources