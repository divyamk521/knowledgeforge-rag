from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    CHROMA_DB_PATH = os.getenv(
        "CHROMA_DB_PATH",
        "app/data/chroma_db"
    )

    RAW_DATA_PATH = os.getenv(
        "RAW_DATA_PATH",
        "app/data/raw"
    )

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 1000)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 200)
    )

    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "knowledgeforge"
    )


settings = Settings()