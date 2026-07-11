from typing import Annotated

from fastapi import APIRouter, File, Form, UploadFile

from app.config.logger import logger
from app.services.upload_service import UploadService

router = APIRouter()


@router.post("/chat")
async def chat(
    query: Annotated[str, Form(...)],
    files: Annotated[list[UploadFile], File(description="Upload one or more files")] = [],
):
    logger.info(f"Received query: {query}")

    uploaded_files = await UploadService.process(files)

    return {
        "success": True,
        "query": query,
        "uploaded_files": [f.model_dump() for f in uploaded_files],
        "message": "Files received successfully",
    }