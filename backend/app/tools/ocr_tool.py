import easyocr

from app.utils.text_cleaner import TextCleaner


class OCRTool:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    def extract_text(self, image_path: str):

        result = self.reader.readtext(
            image_path,
            detail=1,
            paragraph=False
        )

        texts = []
        confidences = []

        for _, text, confidence in result:

            texts.append(text)
            confidences.append(confidence)

        cleaned_text = TextCleaner.clean(
            "\n".join(texts)
        )

        avg_confidence = (
            sum(confidences) / len(confidences)
            if confidences else 0
        )

        return {
            "text": cleaned_text,
            "confidence": round(avg_confidence, 2)
        }


ocr_tool = OCRTool()