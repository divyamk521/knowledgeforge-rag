from pathlib import Path

from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT
from app.retrieval.retriever import get_retriever


def answer_question(question: str):

    retriever = get_retriever()

    documents = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    llm = get_llm()

    prompt = RAG_PROMPT.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(prompt)

    sources = []

    for doc in documents:

        source_name = Path(
            doc.metadata["source"]
        ).name

        page_number = doc.metadata["page"] + 1

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