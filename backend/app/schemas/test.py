from pydantic import BaseModel


class GenerateTestRequest(BaseModel):
    exam_type: str
    paper_type: str
    num_questions: int
    question_source: str = "Mock Questions"
    ca_integration: str = "Off"
    preferences: str = ""
    language: str = "English"


class SubmitTestRequest(BaseModel):
    exam_type: str
    paper_type: str
    total_questions: int
    score: float
    max_score: float
    result_json: str
