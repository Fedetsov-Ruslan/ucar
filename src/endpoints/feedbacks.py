from fastapi import APIRouter, Depends, Query
from typing import List

from src.schemas.response import GetFeedbackResponse
from src.services.feedback_service import FeedbackService


router = APIRouter(
    tags=["feedbacks"],
)


@router.post("/reviews")
def create_feedback(
    text: str,
    feedback_service: FeedbackService = Depends(),
) -> bool:
    """
    Создает новую запись или редактирует существующую

    :param data: Данные для записи
    :return: True, если запись создана или обновлена False в противном случае
    """
    return feedback_service.create_feedback(text=text)


@router.get("/reviews")
def get_feedbacks(
    sentiment: str = Query(..., description="Вид отзыва"),
    feedback_service: FeedbackService = Depends(),
) -> List[GetFeedbackResponse]:
    """
    Возвращает данные по виду отзыва

    :param phone: Вид отзыва
    :return: Данные GetFeedbackResponse
    """
    return feedback_service.get_feedback(sentiment=sentiment)
