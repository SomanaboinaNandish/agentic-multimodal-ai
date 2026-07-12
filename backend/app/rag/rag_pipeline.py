from app.rag.chunker import Chunker
from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store
from app.rag.retriever import retriever


class RAGPipeline:

    @staticmethod
    def ingest(
        text: str,
        source: str = "Unknown"
    ):
        """
        Process document:
        Text -> Chunks -> Embeddings -> FAISS -> Save
        """

        chunks = Chunker.split(text)

        embeddings = embedding_service.embed_documents(chunks)

        vector_store.add_documents(
            chunks=chunks,
            embeddings=embeddings,
            source=source
        )

        # Save FAISS index and metadata
        vector_store.save()

        print(
            f"✅ Ingested {len(chunks)} chunks from {source}"
        )

    @staticmethod
    def retrieve(
        query: str,
        top_k: int = 5
    ):
        """
        Load FAISS if necessary and retrieve relevant chunks.
        """

        if vector_store.index is None:
            vector_store.load()

        return retriever.retrieve(
            query=query,
            top_k=top_k
        )


rag_pipeline = RAGPipeline()