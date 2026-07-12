print(">>> chat.py imported")
from typing import Annotated

from fastapi import APIRouter, File, Form, UploadFile

from app.services.agent_service import AgentService

router = APIRouter()


@router.post("/chat")
async def chat(
    query: Annotated[str, Form(...)],
    files: Annotated[list[UploadFile] | None, File()] = None,
):
    if files is None:
        files = []

    return await AgentService.process(query, files)