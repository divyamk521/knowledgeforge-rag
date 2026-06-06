from app.core.config import settings

print("Embedding Model:", settings.EMBEDDING_MODEL)
print("Chroma DB Path:", settings.CHROMA_DB_PATH)
print("Raw Data Path:", settings.RAW_DATA_PATH)
print("Chunk Size:", settings.CHUNK_SIZE)
print("Chunk Overlap:", settings.CHUNK_OVERLAP)