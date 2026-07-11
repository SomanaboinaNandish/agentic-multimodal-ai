from app.memory.conversation_memory import conversation_memory

conversation_memory.add_user_message("Summarize this PDF")

conversation_memory.add_assistant_message(
    "This PDF describes AI projects."
)

conversation_memory.add_user_message(
    "What is the second project?"
)

print(conversation_memory.get_formatted_history())