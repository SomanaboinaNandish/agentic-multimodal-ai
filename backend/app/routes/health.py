from fastapi import APIRouter

from app.config.logger import logger

router = APIRouter()


@router.get("/health")
async def health():
    logger.info("Health check endpoint called")

    return {
        "status": "healthy"
    }