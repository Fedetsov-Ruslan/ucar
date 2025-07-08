import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from src.endpoints import router
from src.db.sqlite_storage import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    logger.info("✅ База данных и таблицы созданы")
    yield
    logger.info("✅ Приложение остановлено")

app = FastAPI(lifespan=lifespan)

logger = logging.getLogger("uvicorn.error")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    """Обрботчик исключений, связанных с 422 - расширенный вывод в логи"""
    logger.error(f"Ошибка валидации для запроса: {request.url}")
    logger.error(f"Детали ошибки: {exc.errors()}")
    return ORJSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

app.include_router(
    router=router
)
