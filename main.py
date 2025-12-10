from agent.ai_agent import handle_query

print("\n🚀 Kubernetes AI Assistant Running! Ask anything:\n")

while True:
    user = input("You: ").strip()

    if user.lower() in ["exit", "quit", "bye"]:
        print("👋 Exiting Kubernetes AI Assistant.")
        break

    try:
        response = handle_query(user)
        print("\nAI:", response, "\n")
    except Exception as e:
        print("\n❌ Error:", e, "\n")
