from app.tools.ocr_tool import ocr_tool


class ImageService:

    @staticmethod
    def process(image_path: str):

        text = ocr_tool.extract_text(image_path)

        return {
            "success": True,
            "text": text,
            "length": len(text)
        }