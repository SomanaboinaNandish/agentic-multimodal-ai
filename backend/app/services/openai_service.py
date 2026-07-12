from openai import OpenAI

from app.config.settings import settings


class OpenAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def answer(
        self,
        query: str,
        context: str,
        history: str = ""
    ):

        prompt = f"""
You are an intelligent AI assistant.

Use ONLY the provided document context.

Conversation History:
{history}

Document Context:
{context}

Question:
{query}

Answer clearly.
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


openai_service = OpenAIService()