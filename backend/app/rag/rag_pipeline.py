from app.rag.chunker import Chunker
from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store
from app.rag.retriever import retriever


class RAGPipeline:

    @staticmethod
    def ingest(text: str):
        """
        Process a document:
        Text -> Chunks -> Embeddings -> FAISS
        """

        chunks = Chunker.split(text)

        embeddings = embedding_service.embed_documents(chunks)

        vector_store.add_documents(chunks, embeddings)

        print(f"Ingested {len(chunks)} chunks.")

    @staticmethod
    def retrieve(query: str):

        return retriever.retrieve(query)


rag_pipeline = RAGPipeline()