from app.ingestion.vector_store import load_vector_store


SIMILARITY_THRESHOLD = 0.7


def retrieve_documents(question: str):

    vector_store = load_vector_store()

    results = vector_store.similarity_search_with_score(
        question,
        k=5
    )

    filtered_docs = []

    for doc, score in results:

        # Lower score = better similarity in Chroma
        if score < SIMILARITY_THRESHOLD:
            filtered_docs.append(doc)

    return filtered_docs