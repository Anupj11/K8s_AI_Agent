from agent.crew_config import create_ai_agent

assistant = create_ai_agent()

print("\nKubernetes AI Agent Started. Ask anything:\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit", "bye"]:
        break
    response = assistant(query)
    print("\nAI:", response, "\n")
