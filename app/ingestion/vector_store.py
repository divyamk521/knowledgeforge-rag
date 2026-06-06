from langchain_chroma import Chroma

from app.core.config import settings
from app.ingestion.embedder import get_embedding_model


def create_vector_store(chunks):
    """
    Create and persist Chroma vector database.
    """

    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.CHROMA_DB_PATH,
    )

    return vector_store