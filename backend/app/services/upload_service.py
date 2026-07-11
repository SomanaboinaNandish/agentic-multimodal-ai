from typing import List

from fastapi import UploadFile

from app.models.file import UploadedFileInfo
from app.utils.file_detector import detect_file_type


class UploadService:

    @staticmethod
    async def process(files: List[UploadFile]) -> List[UploadedFileInfo]:
        uploaded = []

        for file in files:
            uploaded.append(
                UploadedFileInfo(
                    filename=file.filename,
                    file_type=detect_file_type(file.content_type or ""),
                    content_type=file.content_type or "unknown",
                    size=0,
                )
            )

        return uploaded