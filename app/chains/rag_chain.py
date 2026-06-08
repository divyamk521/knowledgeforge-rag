from pathlib import Path

from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT
from app.retrieval.retriever import retrieve_documents


def answer_question(question: str, chat_history: str = ""):

    documents = retrieve_documents(question)

    if not documents:
        return {
            "answer": (
                "I couldn't find relevant information "
                "in the provided documents."
            ),
            "sources": []
        }

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    llm = get_llm()

    prompt = RAG_PROMPT.invoke(
        {
            "chat_history": chat_history,
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(prompt)

    sources = []

    seen = set()

    for doc in documents:

        source_name = Path(
            doc.metadata["source"]
        ).name

        page_number = doc.metadata["page"] + 1

        key = (source_name, page_number)

        if key not in seen:

            seen.add(key)

            sources.append(
                {
                    "source": source_name,
                    "page": page_number
                }
            )

    return {
        "answer": response.content,
        "sources": sources
    }