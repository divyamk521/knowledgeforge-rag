from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents
from app.ingestion.vector_store import create_vector_store


def index_documents():

    documents = load_documents()

    if not documents:
        raise ValueError("No documents found.")

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("Indexing completed successfully.")