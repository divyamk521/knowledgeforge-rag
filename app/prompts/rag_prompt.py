from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:

"I couldn't find that information in the provided documents."

Do not use your own knowledge.

Context:
{context}

Question:
{question}

Answer:
"""
)