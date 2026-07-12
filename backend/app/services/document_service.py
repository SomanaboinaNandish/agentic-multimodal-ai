from app.models.extracted_content import ExtractedContent
from app.tools.pdf_parser import PDFParser


class DocumentService:

    @staticmethod
    def process(pdf_path: str) -> ExtractedContent:

        extracted_text = PDFParser.extract_text(pdf_path)

        if extracted_text is None:
            extracted_text = ""

        extracted_text = extracted_text.strip()

        return ExtractedContent(
            source="pdf",
            content=extracted_text
        )