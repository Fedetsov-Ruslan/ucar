from sqlalchemy.orm import Session
from fastapi import Depends

from src.db.models import FeedbackData
from src.db.sqlite_storage import get_db
from src.schemas.request import CreateFeedbackRequest
from src.schemas.response import GetFeedbackResponse


class FeedbackRepository:
    def __init__(
        self,
        db: Session = Depends(get_db)
    ):
        self._db = db

    def create_feedback(self, data: CreateFeedbackRequest) -> bool:
        feedback_data = FeedbackData(
            text=data.text,
            sentiment=data.sentiment,
            created_at=data.created_at,
        )
        self._db.add(feedback_data)
        self._db.commit()
        self._db.refresh(feedback_data)
        return True

    def get_feedback(self, sentiment: str) -> list[GetFeedbackResponse]:
        feedbacks = self._db.query(FeedbackData).filter(
            FeedbackData.sentiment == sentiment
        ).all()
        return [
            GetFeedbackResponse(
                id=feedback.id,
                text=feedback.text,
                sentiment=feedback.sentiment,
                created_at=feedback.created_at,
            ) for feedback in feedbacks
        ]
