from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from app.core.config import settings


def load_documents():
    """
    Load all PDFs from app/data/raw/
    """

    documents = []

    pdf_files = Path(settings.RAW_DATA_PATH).glob("*.pdf")

    for pdf_file in pdf_files:
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            docs = loader.load()
            documents.extend(docs)

            print(f"Loaded: {pdf_file.name}")

        except Exception as e:
            print(f"Skipping {pdf_file.name}: {e}")

    return documents