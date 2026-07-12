from app.agent.models import Intent


class IntentDetector:

    @staticmethod
    def detect(query: str) -> Intent:

        query = query.lower()

        # -----------------------
        # YouTube
        # -----------------------
        if (
            "youtube" in query
            or "youtu.be" in query
            or "video" in query
            or "transcript" in query
        ):
            return Intent.YOUTUBE

        # -----------------------
        # Code
        # -----------------------
        if (
            "code" in query
            or "bug" in query
            or "debug" in query
            or "complexity" in query
            or "explain code" in query
        ):
            return Intent.CODE

        # -----------------------
        # Sentiment
        # -----------------------
        if (
            "sentiment" in query
            or "emotion" in query
            or "positive" in query
            or "negative" in query
        ):
            return Intent.SENTIMENT

        # -----------------------
        # Audio
        # -----------------------
        if (
            "audio" in query
            or "transcribe" in query
            or "transcription" in query
            or "speech" in query
            or "voice" in query
        ):
            return Intent.AUDIO

        # -----------------------
        # Summary
        # -----------------------
        if (
            "summarize" in query
            or "summary" in query
            or "summarise" in query
            or "brief" in query
        ):
            return Intent.SUMMARY

        # -----------------------
        # Question Answering
        # -----------------------
        if (
            "?" in query
            or "what" in query
            or "who" in query
            or "when" in query
            or "where" in query
            or "why" in query
            or "how" in query
        ):
            return Intent.QUESTION

        return Intent.UNKNOWN