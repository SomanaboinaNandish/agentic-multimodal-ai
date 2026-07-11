from app.agent.intent_detector import IntentDetector
from app.agent.planner import Planner


class AgentExecutor:

    @staticmethod
    def execute(query: str):

        intent = IntentDetector.detect(query)

        plan = Planner.create(intent)

        return {
            "intent": intent.value,
            "tools": plan.tools
        }