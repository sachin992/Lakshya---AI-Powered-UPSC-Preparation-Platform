from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.dependencies import get_current_user
from app.schemas.mains import MainsEvaluateRequest
from app.services.ai_service import evaluate_mains_answers, ingest_pdf


router = APIRouter(prefix="/mains", tags=["mains"])


@router.post("/upload")
def upload_mains_pdf(thread_id: str, file: UploadFile = File(...), current_user=Depends(get_current_user)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    meta = ingest_pdf(file.file.read(), thread_id=thread_id, filename=file.filename)
    return {"thread_id": thread_id, "metadata": meta}


@router.post("/evaluate")
def evaluate(payload: MainsEvaluateRequest, current_user=Depends(get_current_user)):
    result = evaluate_mains_answers(
        thread_id=payload.thread_id,
        paper=payload.paper,
        marks=payload.marks,
        mode=payload.mode,
        question=payload.question,
    )
    return {"thread_id": payload.thread_id, "evaluation": result}
