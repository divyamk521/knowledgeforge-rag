from fastapi import APIRouter

from backend.schemas import QuestionRequest
from app.chains.rag_chain import answer_question


router = APIRouter()


@router.post("/ask")
def ask_question(
    request: QuestionRequest
):

    result = answer_question(
        question=request.question,
        chat_history=request.chat_history
    )

    return result