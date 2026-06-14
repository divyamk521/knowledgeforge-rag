from functools import lru_cache

from rank_bm25 import BM25Okapi

from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents


@lru_cache(maxsize=1)
def get_bm25():

    documents = load_documents()

    chunks = split_documents(documents)

    tokenized_chunks = [
        chunk.page_content.split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)

    print("BM25 loaded.")

    return bm25, chunks


def bm25_search(
    question: str,
    top_k: int = 10
):

    bm25, chunks = get_bm25()

    tokenized_query = question.split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    top_documents = [
        chunks[i]
        for i in ranked_indices[:top_k]
    ]

    return top_documents