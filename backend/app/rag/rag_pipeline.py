from app.rag.chunker import Chunker
from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store
from app.rag.retriever import retriever


class RAGPipeline:

    @staticmethod
    def ingest(text: str):
        """
        Process a document:
        Text -> Chunks -> Embeddings -> FAISS -> Save
        """

        chunks = Chunker.split(text)

        embeddings = embedding_service.embed_documents(chunks)

        vector_store.add_documents(chunks, embeddings)

        # Save FAISS index and documents
        vector_store.save()

        print(f"Ingested {len(chunks)} chunks.")

    @staticmethod
    def retrieve(query: str, top_k: int = 5):
        """
        Load FAISS if necessary and retrieve relevant chunks.
        """

        # Load saved index if not already loaded
        if vector_store.index is None:
            vector_store.load()

        return retriever.retrieve(
            query=query,
            top_k=top_k
        )


rag_pipeline = RAGPipeline()