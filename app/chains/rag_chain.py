from pathlib import Path

from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT
from app.retrieval.retriever import retrieve_documents
from app.chains.question_rewriter import rewrite_question
from app.utils.logger import log_query


def answer_question(
    question: str,
    chat_history: str = ""
):

    standalone_question = rewrite_question(
        question=question,
        chat_history=chat_history
    )

    print("\n========== STANDALONE QUESTION ==========")
    print(standalone_question)
    print("=========================================\n")

    documents = retrieve_documents(
        standalone_question
    )

    if not documents:

        result = {
            "answer": (
                "I couldn't find relevant information "
                "in the provided documents."
            ),
            "sources": [],
            "rewritten_question": standalone_question
        }

        log_query(
            question,
            standalone_question,
            result["answer"],
            result["sources"]
        )

        return result

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    llm = get_llm()

    prompt = RAG_PROMPT.invoke(
        {
            "chat_history": chat_history,
            "context": context,
            "question": standalone_question
        }
    )

    response = llm.invoke(prompt)

    sources = []

    seen = set()

    for doc in documents:

        source_name = Path(
            doc.metadata["source"]).name

        page_number = doc.metadata["page"] + 1

        key = (
            source_name,
            page_number
        )

        if key not in seen:

            seen.add(key)

            sources.append(
                {
                    "source": source_name,
                    "page": page_number
                }
            )

    result = {
        "answer": response.content,
        "sources": sources,
        "rewritten_question": standalone_question
    }

    log_query(
        question,
        standalone_question,
        result["answer"],
        result["sources"]
    )

    return result