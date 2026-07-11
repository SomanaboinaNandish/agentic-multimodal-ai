from app.services.gemini_service import gemini_service

text = """
FastAPI is a modern web framework.

It is used to build APIs.

It is very fast.

It supports async programming.
"""

result = gemini_service.summarize(text)

print(result)