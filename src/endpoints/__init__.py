from fastapi import APIRouter

from .feedbacks import router as feedback_router

router = APIRouter()

router.include_router(feedback_router)
