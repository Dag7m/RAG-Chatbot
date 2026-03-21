from retrieval.retriever import get_retriever
from retrieval.generator import generate_answer
from utils.memory import add_to_history, get_history_text

def ask_question(query):
    retriever = get_retriever()  # ALWAYS refresh

    docs = retriever.invoke(query)

    context_parts = []
    for doc in docs:
        source = doc.metadata.get("source", "Unknown Source")
        context_parts.append(f"Source: {source}\n{doc.page_content}\n")
    context = "\n".join(context_parts)

    history_text = get_history_text()

    full_context = f"""
Chat History:
{history_text}

Retrieved Context:
{context}
"""

    answer = generate_answer(query, full_context)

    sources = [doc.page_content for doc in docs[:2]]

    add_to_history(query, answer, sources)

    return answer, sources