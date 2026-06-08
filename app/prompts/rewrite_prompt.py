from langchain_core.prompts import ChatPromptTemplate


REWRITE_PROMPT = ChatPromptTemplate.from_template(
    """
Given the chat history and the latest user question,
rewrite the question into a standalone question.

The standalone question should contain all context
needed for retrieval.

If the question is already standalone,
return it unchanged.

Chat History:
{chat_history}

Question:
{question}

Standalone Question:
"""
)