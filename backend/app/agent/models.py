from enum import Enum
from pydantic import BaseModel


class Intent(str, Enum):
    SUMMARY = "summary"
    SENTIMENT = "sentiment"
    CODE = "code"
    YOUTUBE = "youtube"
    QUESTION = "question"
    UNKNOWN = "unknown"
    AUDIO = "audio"


class ExecutionPlan(BaseModel):
    intent: Intent
    tools: list[str]