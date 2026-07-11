from app.models.file import FileType


IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/jpg"
}

PDF_TYPES = {
    "application/pdf"
}

AUDIO_TYPES = {
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
    "audio/m4a"
}


def detect_file_type(content_type: str) -> FileType:

    if content_type in IMAGE_TYPES:
        return FileType.IMAGE

    if content_type in PDF_TYPES:
        return FileType.PDF

    if content_type in AUDIO_TYPES:
        return FileType.AUDIO

    return FileType.UNKNOWN