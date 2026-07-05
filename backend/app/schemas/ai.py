from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    thread_id: str


class ChatResponse(BaseModel):
    thread_id: str
    response: str


class FeedbackRequest(BaseModel):
    rating: int = Field(ge=1, le=5)
    feedback_text: str = ""


class GenericMessage(BaseModel):
    message: str
