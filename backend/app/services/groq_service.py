from openai import OpenAI

from app.config.settings import settings


class GroqService:

    def __init__(self):

        print("Using Groq Key:", settings.GROQ_API_KEY[:10] + "...")

        self.client = OpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

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

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    def answer(
        self,
        query: str,
        context: str,
        history: str = ""
    ):

        prompt = f"""
You are an intelligent AI assistant.

Use the conversation history to understand follow-up questions.

Use ONLY the information provided in the document context.

If the answer is not present, reply:

"I couldn't find that information in the uploaded document."

========================
Conversation History
========================

{history}

========================
Document Context
========================

{context}

========================
Current Question
========================

{query}

Provide a clear and detailed answer.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content


groq_service = GroqService()