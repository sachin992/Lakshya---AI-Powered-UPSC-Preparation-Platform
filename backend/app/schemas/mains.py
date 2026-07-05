from pydantic import BaseModel


class MainsEvaluateRequest(BaseModel):
    thread_id: str
    paper: str
    marks: int
    mode: str
    question: str | None = None
