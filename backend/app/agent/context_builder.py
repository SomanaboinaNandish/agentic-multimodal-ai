from typing import List

from app.models.extracted_content import ExtractedContent


class ContextBuilder:
    """
    Builds a unified context from multiple extracted sources.
    """

    @staticmethod
    def build(query: str, contents: List[ExtractedContent]) -> str:
        sections = []

        sections.append("========== USER QUERY ==========")
        sections.append(query)
        sections.append("")

        for item in contents:
            sections.append(f"========== {item.source.upper()} ==========")
            sections.append(item.content)
            sections.append("")

        return "\n".join(sections)