import shutil
from pathlib import Path

from app.core.config import settings
from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents
from app.ingestion.vector_store import create_vector_store


def index_documents():

    chroma_path = Path(settings.CHROMA_DB_PATH)

    if chroma_path.exists():
        shutil.rmtree(chroma_path)

    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("Indexing completed successfully.")