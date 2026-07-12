from openai import OpenAI

from app.config.settings import settings


class GroqService:

    def __init__(self):

        print("Using Groq Key:", settings.GROQ_API_KEY[:10] + "...")

        self.client = OpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

    # -----------------------------------
    # Internal Helper
    # -----------------------------------

    def _chat(self, system_prompt: str, user_prompt: str):

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    # -----------------------------------
    # General Summary
    # -----------------------------------

    def summarize(self, context: str):

        prompt = f"""
Summarize the following content.

Return EXACTLY in this format:

One-line Summary:
...

Three Key Points:
- ...
- ...
- ...

Five-Sentence Summary:
1.
2.
3.
4.
5.

Content:

{context}
"""

        return self._chat(
            "You are an expert summarization assistant.",
            prompt
        )

    # -----------------------------------
    # Audio Summary
    # -----------------------------------

    def summarize_audio(self, transcript: str):

        prompt = f"""
The following is an audio transcript.

Return:

One-line Summary:
...

Three Key Points:
- ...
- ...
- ...

Five-Sentence Summary:
1.
2.
3.
4.
5.

Transcript:

{transcript}
"""

        return self._chat(
            "You summarize audio transcripts.",
            prompt
        )

    # -----------------------------------
    # Sentiment Analysis
    # -----------------------------------

    def sentiment(self, text: str):

        prompt = f"""
Analyze the sentiment of the following text.

Return:

Sentiment:
Positive / Negative / Neutral

Confidence:
0-100%

Reason:
One sentence.

Text:

{text}
"""

        return self._chat(
            "You are an expert sentiment analysis assistant.",
            prompt
        )

    # -----------------------------------
    # Code Explanation
    # -----------------------------------

    def explain_code(self, code: str):

        prompt = f"""
Analyze the following code.

Return:

Language:

Purpose:

Step-by-step Explanation:

Possible Bugs:

Time Complexity:

Space Complexity:

Suggestions:

Code:

{code}
"""

        return self._chat(
            "You are a senior software engineer.",
            prompt
        )

    # -----------------------------------
    # RAG Question Answering
    # -----------------------------------

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

If the answer is not present, reply exactly:

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

        return self._chat(
            "You are a helpful AI assistant.",
            prompt
        )


groq_service = GroqService()