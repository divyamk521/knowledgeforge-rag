from langchain_chroma import Chroma

from app.core.config import settings
from app.ingestion.embedder import get_embedding_model


def create_vector_store(chunks):
    """
    Create vector database and persist embeddings.
    """

    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name=settings.COLLECTION_NAME,
        persist_directory=settings.CHROMA_DB_PATH,
        embedding_function=embeddings,
    )

    vector_store.add_documents(chunks)

    return vector_store


def load_vector_store():
    """
    Load existing vector database.
    """

    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name=settings.COLLECTION_NAME,
        persist_directory=settings.CHROMA_DB_PATH,
        embedding_function=embeddings,
    )

    return vector_store