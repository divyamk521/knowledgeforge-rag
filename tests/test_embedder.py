from app.ingestion.embedder import get_embedding_model


embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "What is Retrieval Augmented Generation?"
)

print(f"Vector dimension: {len(vector)}")

print("\nFirst 10 values:")
print(vector[:10])