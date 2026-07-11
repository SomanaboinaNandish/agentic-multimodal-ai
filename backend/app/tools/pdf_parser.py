import pdfplumber

from app.utils.text_cleaner import TextCleaner


class PDFParser:

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        extracted_pages = []

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_pages.append(page_text)

        text = "\n".join(extracted_pages)

        return TextCleaner.clean(text)