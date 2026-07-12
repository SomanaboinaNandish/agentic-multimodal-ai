from app.agent.models import ExecutionPlan, Intent


class Planner:

    @staticmethod
    def create(intent: Intent) -> ExecutionPlan:

        # -----------------------
        # Summary
        # -----------------------

        if intent == Intent.SUMMARY:

            return ExecutionPlan(
                intent=intent,
                tools=[
                    "summarizer"
                ]
            )

        # -----------------------
        # Audio
        # -----------------------

        if intent == Intent.AUDIO:

            return ExecutionPlan(
                intent=intent,
                tools=[
                    "audio_transcriber",
                    "audio_summarizer"
                ]
            )

        # -----------------------
        # Sentiment Analysis
        # -----------------------

        if intent == Intent.SENTIMENT:

            return ExecutionPlan(
                intent=intent,
                tools=[
                    "sentiment"
                ]
            )

        # -----------------------
        # Code Explanation
        # -----------------------

        if intent == Intent.CODE:

            return ExecutionPlan(
                intent=intent,
                tools=[
                    "code_explainer"
                ]
            )

        # -----------------------
        # YouTube
        # -----------------------

        if intent == Intent.YOUTUBE:

            return ExecutionPlan(
                intent=intent,
                tools=[
                    "youtube_transcript",
                    "summarizer"
                ]
            )

        # -----------------------
        # General Question Answering
        # -----------------------

        return ExecutionPlan(
            intent=intent,
            tools=[
                "rag_qa"
            ]
        )