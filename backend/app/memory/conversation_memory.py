from collections import deque


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(self, max_messages: int = 10):

        self.history = deque(maxlen=max_messages)

    def add_user_message(self, message: str):

        self.history.append({
            "role": "user",
            "content": message
        })

    def add_assistant_message(self, message: str):

        self.history.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):

        return list(self.history)

    def get_formatted_history(self):

        if not self.history:
            return ""

        text = []

        for item in self.history:

            role = item["role"].capitalize()

            text.append(f"{role}: {item['content']}")

        return "\n".join(text)

    def clear(self):

        self.history.clear()


conversation_memory = ConversationMemory()