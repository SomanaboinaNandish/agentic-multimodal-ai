from app.tools.pdf_parser import PDFParser


class DocumentService:

    @staticmethod
    def process(pdf_path: str):

        extracted_text = PDFParser.extract_text(pdf_path)

        return {
            "success": True,
            "text": extracted_text,
            "length": len(extracted_text)
        }