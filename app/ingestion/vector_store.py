from chromadb import PersistentClient
from langchain_chroma import Chroma

from app.core.config import settings
from app.ingestion.embedder import get_embedding_model


def create_vector_store(chunks):
    """
    Recreate collection and store embeddings.
    """

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

    return vector_store


def load_vector_store():
    """
    Load existing collection.
    """

    embeddings = get_embedding_model()

    client = PersistentClient(
        path=settings.CHROMA_DB_PATH
    )

    vector_store = Chroma(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding_function=embeddings,
    )

    return vector_store