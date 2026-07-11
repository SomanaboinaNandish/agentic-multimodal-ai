from typing import List


class Chunker:

    @staticmethod
    def split(text: str, chunk_size=1000, overlap=250) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks