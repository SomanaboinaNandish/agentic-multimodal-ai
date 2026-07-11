from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingService:

    def __init__(self):
        # Loads once when the service is created
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, chunks: List[str]):
        """
        Convert multiple text chunks into embeddings.
        """
        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True
        )

        return embeddings

    def embed_query(self, query: str):
        """
        Convert a user query into an embedding.
        """
        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding


embedding_service = EmbeddingService()