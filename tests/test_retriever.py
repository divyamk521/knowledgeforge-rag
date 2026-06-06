from app.retrieval.retriever import get_retriever


query = input("Enter your question: ")

retriever = get_retriever()

results = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results, start=1):
    print(f"\nChunk {i}")
    print("-" * 50)
    print(doc.page_content[:300])

    print("\nMetadata:")
    print(doc.metadata)