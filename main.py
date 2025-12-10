from agent.k8s_agent import K8sAgent
from agent.crew_config import create_ai_agent

k8s = K8sAgent()
assistant = create_ai_agent(k8s)

print("Kubernetes AI Agent Started. Ask anything:\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = assistant(query)
    print("\nAI Agent:", response, "\n")
