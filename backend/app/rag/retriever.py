from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store


class Retriever:

    @staticmethod
    def retrieve(
        query: str,
        top_k: int = 5
    ):
        """
        Retrieve the most relevant chunks from FAISS.
        Each result contains:
        {
            "source": "...",
            "content": "..."
        }
        """

        query_embedding = embedding_service.embed_query(query)

        results = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return results


retriever = Retriever()