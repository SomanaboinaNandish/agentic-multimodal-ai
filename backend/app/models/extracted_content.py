from pydantic import BaseModel
from typing import Optional


class ExtractedContent(BaseModel):
    """
    Represents text extracted from one input source
    (PDF, Image, Audio, etc.).
    """

    source: str
    content: str

    # Optional fields
    confidence: Optional[float] = None
    page: Optional[int] = None