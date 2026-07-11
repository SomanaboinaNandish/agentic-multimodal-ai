from app.rag.embedding_service import embedding_service

chunks = [
    "FastAPI is used to build APIs.",
    "Python is a programming language.",
    "Gemini is a large language model."
]

embeddings = embedding_service.embed_documents(chunks)

print("Number of vectors:", len(embeddings))
print("Vector dimension:", len(embeddings[0]))

query = embedding_service.embed_query("What is FastAPI?")

print("Query dimension:", len(query))