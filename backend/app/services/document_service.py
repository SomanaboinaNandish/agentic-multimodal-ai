from app.models.extracted_content import ExtractedContent
from app.tools.pdf_parser import PDFParser
from app.tools.pdf_ocr_tool import pdf_ocr_tool


class DocumentService:

    @staticmethod
    def process(pdf_path: str) -> ExtractedContent:

        extracted_text = PDFParser.extract_text(
            pdf_path
        )

        if extracted_text is None:
            extracted_text = ""

        extracted_text = extracted_text.strip()

        # OCR fallback

        if len(extracted_text) < 20:

            print("Running OCR on scanned PDF...")

            extracted_text = pdf_ocr_tool.extract_text(
                pdf_path
            )

        return ExtractedContent(
            source="pdf",
            content=extracted_text
        )