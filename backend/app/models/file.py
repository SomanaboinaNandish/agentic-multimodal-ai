from enum import Enum
from pydantic import BaseModel


class FileType(str, Enum):
    IMAGE = "image"
    PDF = "pdf"
    AUDIO = "audio"
    UNKNOWN = "unknown"


class UploadedFileInfo(BaseModel):
    filename: str
    file_type: FileType
    content_type: str
    size: int