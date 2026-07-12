from app.agent.models import ExecutionPlan, Intent


class Planner:

    @staticmethod
    def create(intent: Intent) -> ExecutionPlan:

        if intent == Intent.SUMMARY:
            return ExecutionPlan(
                intent=intent,
                tools=["summarizer"]
            )
        
        if intent == Intent.AUDIO:
            return ExecutionPlan(
    intent=intent,
    tools=[
        "audio_transcriber",
        "rag_qa"
    ]
)

        if intent == Intent.SENTIMENT:
            return ExecutionPlan(
                intent=intent,
                tools=["sentiment"]
            )

        if intent == Intent.CODE:
            return ExecutionPlan(
                intent=intent,
                tools=["code_explainer"]
            )

        if intent == Intent.YOUTUBE:
            return ExecutionPlan(
                intent=intent,
                tools=[
                    "youtube_transcript",
                    "summarizer"
                ]
            )

        # NEW: Default to RAG Question Answering
        return ExecutionPlan(
            intent=intent,
            tools=["rag_qa"]
        )