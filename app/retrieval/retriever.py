from app.ingestion.vector_store import load_vector_store
from app.retrieval.reranker import rerank_documents


def retrieve_documents(
    question: str
):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 20,
            "fetch_k": 30
        }
    )

    documents = retriever.invoke(question)

    reranked_documents = rerank_documents(
        question=question,
        documents=documents,
        top_k=5
    )

    return reranked_documents