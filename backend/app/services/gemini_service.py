import google.generativeai as genai

from app.config.settings import settings


class GeminiService:

    def __init__(self):

        genai.configure(api_key=settings.GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def summarize(self, context: str):

        prompt = f"""
You are an AI assistant.

Summarize the following content.

Return:
1. One-line summary
2. Three bullet points
3. Five-sentence summary

Content:
{context}
"""

        response = self.model.generate_content(prompt)

        return response.text

    def answer(self, query: str, context: str):

        prompt = f"""
You are an intelligent document assistant.

Use ONLY the information provided below.

If the answer is not present in the context, reply:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{query}

Provide a clear and detailed answer.
"""

        response = self.model.generate_content(prompt)

        return response.text


gemini_service = GeminiService()