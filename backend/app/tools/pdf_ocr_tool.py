import os
import tempfile

import fitz

from app.tools.ocr_tool import ocr_tool


class PDFOCRTool:

    def extract_text(self, pdf_path: str):

        doc = fitz.open(pdf_path)

        extracted_text = []

        for page in doc:

            pix = page.get_pixmap(
                dpi=300
            )

            with tempfile.NamedTemporaryFile(
                suffix=".png",
                delete=False
            ) as temp:

                pix.save(temp.name)

                text = ocr_tool.extract_text(
                    temp.name
                )

                extracted_text.append(text)

                os.remove(temp.name)

        doc.close()

        return "\n".join(extracted_text)


pdf_ocr_tool = PDFOCRTool()