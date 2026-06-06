from app.ingestion.loader import load_documents
from app.ingestion.chunker import split_documents


documents = load_documents()

chunks = split_documents(documents)

print(f"\nTotal documents loaded: {len(documents)}")
print(f"Total chunks created: {len(chunks)}")

if chunks:
    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk preview:\n")
    print(chunks[10].page_content[:500])

else:
    print("No chunks created.")