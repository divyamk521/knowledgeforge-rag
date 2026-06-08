from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are a helpful AI assistant.

Use ONLY the provided context and chat history.

If the answer is not present in the context, say:

"I couldn't find that information in the provided documents."

Chat History:
{chat_history}

Context:
{context}

Question:
{question}

Answer:
"""
)