from app.rag.embedding_service import embedding_service
from app.rag.vector_store import vector_store

chunks = [

    "FastAPI is used to build APIs.",

    "Python is a programming language.",

    "Gemini is Google's AI model.",

    "FAISS performs vector similarity search.",

    "React is used for frontend."
]

embeddings = embedding_service.embed_documents(chunks)

vector_store.add_documents(chunks, embeddings)

query = "How do I build APIs?"

query_embedding = embedding_service.embed_query(query)

results = vector_store.search(query_embedding)

print("\nRetrieved Chunks:\n")

for r in results:
    print("-", r)