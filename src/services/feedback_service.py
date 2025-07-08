from datetime import datetime
from fastapi import Depends

from src.schemas.request import CreateFeedbackRequest
from src.schemas.response import GetFeedbackResponse
from src.schemas.sentiments import SENTIMENT_KEYWORDS, Sentiment
from src.repository.feedback_repository import FeedbackRepository


class FeedbackService:
    def __init__(
        self,
        feedback_repository: FeedbackRepository = Depends(),
    ):
        self.feedback_repository = feedback_repository

    def create_feedback(self, text: str) -> bool:
        sentiment = Sentiment.NEUTRAL
        for keyword, sentiment_value in SENTIMENT_KEYWORDS.items():
            if keyword in text.lower():
                sentiment = sentiment_value
                break

        data = CreateFeedbackRequest(
            text=text,
            sentiment=sentiment,
            created_at=datetime.now().isoformat(),
        )
        return self.feedback_repository.create_feedback(data)

    def get_feedback(self, sentiment: str) -> list[GetFeedbackResponse]:
        return self.feedback_repository.get_feedback(sentiment=sentiment)
