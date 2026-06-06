from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents
from app.ingestion.vector_store import create_vector_store


def index_documents():
    """
    Complete ingestion pipeline.

    PDF → Documents → Chunks → Vector Store
    """

    print("Loading documents...")
    documents = load_documents()

    print(f"Loaded {len(documents)} pages.")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating vector store...")
    create_vector_store(chunks)

    print("Indexing completed successfully!")