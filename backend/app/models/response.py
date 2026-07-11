from typing import List

from pydantic import BaseModel


class ChatResponse(BaseModel):
    success: bool
    message: str
    response: str
    plan: List[str]