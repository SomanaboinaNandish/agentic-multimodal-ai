import easyocr

from app.utils.text_cleaner import TextCleaner


class OCRTool:
    def __init__(self):
        # Initialize once
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    def extract_text(self, image_path: str):

        result = self.reader.readtext(
            image_path,
            detail=0,
            paragraph=True
        )

        text = "\n".join(result)

        return TextCleaner.clean(text)


ocr_tool = OCRTool()