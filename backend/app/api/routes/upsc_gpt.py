from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Feedback
from app.dependencies import get_current_user
from app.schemas.ai import ChatRequest, ChatResponse, FeedbackRequest, GenericMessage
from app.services.ai_service import chat, ingest_pdf, thread_document_metadata


router = APIRouter(prefix="/upsc-gpt", tags=["upsc-gpt"])


@router.post("/chat", response_model=ChatResponse)
def chat_with_gpt(payload: ChatRequest, current_user=Depends(get_current_user)):
    try:
        response = chat(payload.message, payload.thread_id)
        return ChatResponse(thread_id=payload.thread_id, response=response)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Chat failed: {exc}")


@router.post("/upload", response_model=dict)
def upload_pdf(thread_id: str, file: UploadFile = File(...), current_user=Depends(get_current_user)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    content = file.file.read()
    meta = ingest_pdf(content, thread_id=thread_id, filename=file.filename)
    return {"thread_id": thread_id, "metadata": meta}


@router.get("/thread/{thread_id}", response_model=dict)
def thread_meta(thread_id: str, current_user=Depends(get_current_user)):
    return {"thread_id": thread_id, "metadata": thread_document_metadata(thread_id)}


@router.post("/feedback", response_model=GenericMessage)
def submit_feedback(payload: FeedbackRequest, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    row = Feedback(user_id=current_user.id, rating=payload.rating, feedback_text=payload.feedback_text)
    db.add(row)
    db.commit()
    return GenericMessage(message="Feedback submitted")
