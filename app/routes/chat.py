from fastapi import APIRouter
from app.models.chat_model import ChatRequest
from app.services.rag_services import ask_question

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    #hello bhaijaan

    answer = ask_question(
        request.question,
        request.chat_history
    )


    return {
        "answer": answer
    }