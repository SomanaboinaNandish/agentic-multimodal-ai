from app.agent.models import Intent


class IntentDetector:

    @staticmethod
    def detect(query: str) -> Intent:

        query = query.lower()

        # Highest priority: YouTube
        if "youtube" in query or "youtu.be" in query:
            return Intent.YOUTUBE

        # Code explanation
        if (
            "code" in query
            or "bug" in query
            or "debug" in query
            or "complexity" in query
        ):
            return Intent.CODE

        # Sentiment
        if "sentiment" in query or "emotion" in query:
            return Intent.SENTIMENT

        # Summary
        if (
            "summarize" in query
            or "summary" in query
            or "summarise" in query
        ):
            return Intent.SUMMARY

        # General question
        if "?" in query:
            return Intent.QUESTION

        return Intent.UNKNOWN