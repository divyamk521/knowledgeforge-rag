from app.ingestion.vector_store import load_vector_store

vector_store = load_vector_store()

print("Vector store loaded successfully.")

print(
    f"Number of vectors: {vector_store._collection.count()}"
)