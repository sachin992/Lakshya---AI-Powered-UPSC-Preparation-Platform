from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_current_user
from app.services.puzzle_service import create_grid, pick_question, score_answer


router = APIRouter(prefix="/puzzle", tags=["puzzle"])


class PuzzleInitRequest(BaseModel):
    seed: str
    grid_size: int
    total_questions: int


class PuzzleQuestionRequest(BaseModel):
    category: str


class PuzzleAnswerRequest(BaseModel):
    selected: str
    correct: str


@router.post("/init")
def init_puzzle(payload: PuzzleInitRequest, current_user=Depends(get_current_user)):
    return create_grid(payload.seed, payload.grid_size, payload.total_questions)


@router.post("/question")
def question(payload: PuzzleQuestionRequest, current_user=Depends(get_current_user)):
    return pick_question(payload.category)


@router.post("/score")
def score(payload: PuzzleAnswerRequest, current_user=Depends(get_current_user)):
    return {"score_delta": score_answer(payload.selected, payload.correct)}
