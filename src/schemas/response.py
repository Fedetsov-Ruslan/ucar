from pydantic import BaseModel


class GetFeedbackResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str
