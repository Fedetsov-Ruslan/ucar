from pydantic import BaseModel


class CreateFeedbackRequest(BaseModel):
    text: str
    sentiment: str
    created_at: str
