from app.ingestion.vector_store import load_vector_store


def get_retriever():
    """
    Create MMR retriever.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20,
        }
    )

    return retriever