from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.models import TestAttempt


def get_dashboard_summary(db: Session, user_id: int):
    total_tests = db.query(func.count(TestAttempt.id)).filter(TestAttempt.user_id == user_id).scalar() or 0
    avg_score = db.query(func.avg(TestAttempt.score)).filter(TestAttempt.user_id == user_id).scalar() or 0
    total_max = db.query(func.sum(TestAttempt.max_score)).filter(TestAttempt.user_id == user_id).scalar() or 0
    total_scored = db.query(func.sum(TestAttempt.score)).filter(TestAttempt.user_id == user_id).scalar() or 0
    accuracy = (total_scored / total_max * 100.0) if total_max else 0.0

    return {
        "tests_completed": int(total_tests),
        "avg_score": round(float(avg_score), 2),
        "accuracy_percent": round(float(accuracy), 2),
    }
