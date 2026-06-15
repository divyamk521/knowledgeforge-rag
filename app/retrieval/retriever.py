from app.ingestion.vector_store import load_vector_store
from app.retrieval.reranker import rerank_documents
from app.retrieval.bm25_retriever import bm25_search


def retrieve_documents(
    question: str
):

    vector_store = load_vector_store()

    vector_retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 10,
            "fetch_k": 20
        }
    )

    vector_documents = vector_retriever.invoke(
        question
    )

    bm25_documents = bm25_search(
        question,
        top_k=10
    )

    combined_documents = (
        vector_documents +
        bm25_documents
    )

    unique_documents = []

    seen = set()

    for doc in combined_documents:

        content = doc.page_content

        if content not in seen:

            seen.add(content)

            unique_documents.append(doc)

    reranked_documents, confidence_score = (
        rerank_documents(
            question=question,
            documents=unique_documents,
            top_k=5
        )
    )

    return reranked_documents, confidence_score