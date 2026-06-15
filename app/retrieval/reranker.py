from functools import lru_cache

from sentence_transformers import CrossEncoder


@lru_cache(maxsize=1)
def get_reranker():

    model = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    print("Cross Encoder loaded.")

    return model


def rerank_documents(
    question,
    documents,
    top_k=5
):

    if not documents:
        return [], 0

    reranker = get_reranker()

    pairs = [
        (question, doc.page_content)
        for doc in documents
    ]

    scores = reranker.predict(pairs)

    scored_docs = list(
        zip(documents, scores)
    )

    scored_docs.sort(
        key=lambda x: x[1],
        reverse=True
    )

    top_documents = [
        doc
        for doc, score in scored_docs[:top_k]
    ]

    best_score = float(
        scored_docs[0][1]
    )

    return top_documents, best_score