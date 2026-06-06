from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents
from app.ingestion.vector_store import create_vector_store


documents = load_documents()

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print(f"\nDocuments loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")

print("\nVector database created successfully!")