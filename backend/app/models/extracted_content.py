from pydantic import BaseModel


class ExtractedContent(BaseModel):
    """
    Represents text extracted from one input source
    (PDF, Image, Audio, etc.).
    """

    source: str
    content: str