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

    return response.content