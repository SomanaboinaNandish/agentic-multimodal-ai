from app.agent.agent_executor import AgentExecutor

queries = [
    "Summarize this PDF",
    "Analyze sentiment",
    "Explain code",
    "Open YouTube and summarize",
    "What is RAG?"
]

for q in queries:

    print("=" * 50)

    result = AgentExecutor.execute(q)

    print("Query :", q)
    print("Intent:", result["intent"])
    print("Tools :", result["tools"])