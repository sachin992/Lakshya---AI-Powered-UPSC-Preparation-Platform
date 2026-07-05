import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import TestAttempt
from app.dependencies import get_current_user
from app.schemas.test import GenerateTestRequest, SubmitTestRequest
from app.services.ai_service import generate_questions


router = APIRouter(prefix="/tests", tags=["tests"])


@router.post("/generate")
def generate_test(payload: GenerateTestRequest, current_user=Depends(get_current_user)):
    questions = generate_questions(
        exam_type=payload.exam_type,
        paper_type=payload.paper_type,
        num_questions=payload.num_questions,
        question_source=payload.question_source,
        ca_integration=payload.ca_integration,
        preferences=payload.preferences,
        language=payload.language,
    )
    return {"questions": questions}


@router.post("/submit")
def submit_test(payload: SubmitTestRequest, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    row = TestAttempt(
        user_id=current_user.id,
        exam_type=payload.exam_type,
        paper_type=payload.paper_type,
        total_questions=payload.total_questions,
        score=payload.score,
        max_score=payload.max_score,
        result_json=payload.result_json,
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"message": "Test saved", "attempt_id": row.id}


@router.get("/history")
def get_history(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    rows = (
        db.query(TestAttempt)
        .filter(TestAttempt.user_id == current_user.id)
        .order_by(TestAttempt.created_at.desc())
        .all()
    )
    return [
        {
            "id": row.id,
            "exam_type": row.exam_type,
            "paper_type": row.paper_type,
            "total_questions": row.total_questions,
            "score": row.score,
            "max_score": row.max_score,
            "result_json": json.loads(row.result_json or "{}"),
            "created_at": row.created_at.isoformat(),
        }
        for row in rows
    ]
