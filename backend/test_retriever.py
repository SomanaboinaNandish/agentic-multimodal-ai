from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store
from app.rag.retriever import retriever

chunks = [
    "FastAPI is a modern Python framework.",
    "Gemini is Google's large language model.",
    "FAISS is used for vector similarity search.",
    "React is a frontend library.",
    "Python is used for AI."
]

embeddings = embedding_service.embed_documents(chunks)

vector_store.add_documents(chunks, embeddings)

results = retriever.retrieve("Which framework builds APIs?")

print("\nRetrieved:\n")

for r in results:
    print(r)