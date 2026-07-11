from app.rag.rag_pipeline import rag_pipeline

document = """
FastAPI is a modern Python framework used to build APIs.

FAISS is a vector database used for similarity search.

Gemini is Google's large language model.

React is used for frontend development.
"""

rag_pipeline.ingest(document)

results = rag_pipeline.retrieve(
    "Which framework is used to build APIs?"
)

print("\nRetrieved Chunks:\n")

for r in results:
    print("-", r)