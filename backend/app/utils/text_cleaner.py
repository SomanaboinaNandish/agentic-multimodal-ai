import re


class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        # Remove null characters
        text = text.replace("\x00", "")

        # Normalize newlines
        text = re.sub(r"\n+", "\n", text)

        # Normalize spaces
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()