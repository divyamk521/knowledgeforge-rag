from app.ingestion.loader import load_documents


documents = load_documents()

print(f"\nTotal pages loaded: {len(documents)}")

print("\nFirst document metadata:")
print(documents[0].metadata)

print("\nContent preview:\n")
print(documents[0].page_content[:500])