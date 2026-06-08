from app.llm.groq_client import get_llm
from app.prompts.rewrite_prompt import REWRITE_PROMPT


def rewrite_question(
    question: str,
    chat_history: str = ""
) -> str:

    if not chat_history.strip():
        return question

    llm = get_llm()

    prompt = REWRITE_PROMPT.invoke(
        {
            "chat_history": chat_history,
            "question": question
        }
    )

    response = llm.invoke(prompt)

    return response.content.strip()