from app.models.extracted_content import ExtractedContent
from app.tools.ocr_tool import ocr_tool


class ImageService:

    @staticmethod
    def process(image_path: str) -> ExtractedContent:

        ocr_result = ocr_tool.extract_text(image_path)

        return ExtractedContent(
            source="image",
            content=ocr_result["text"],
            confidence=ocr_result["confidence"]
        )