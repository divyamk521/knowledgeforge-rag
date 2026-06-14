from functools import lru_cache

from chromadb import PersistentClient
from langchain_chroma import Chroma

from app.core.config import settings
from app.ingestion.embedder import get_embedding_model


def create_vector_store(chunks):

    embeddings = get_embedding_model()

    client = PersistentClient(
        path=settings.CHROMA_DB_PATH
    )

    try:
        client.delete_collection(
            settings.COLLECTION_NAME
        )
    except Exception:
        pass

    vector_store = Chroma(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings,
    )

    vector_store.add_documents(chunks)

    load_vector_store.cache_clear()

    return vector_store


@lru_cache(maxsize=1)
def load_vector_store():

    embeddings = get_embedding_model()

    client = PersistentClient(
        path=settings.CHROMA_DB_PATH
    )

    vector_store = Chroma(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings,
    )

    print("Vector store loaded.")

    return vector_store