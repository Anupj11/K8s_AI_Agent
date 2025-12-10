from crewai import Agent
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_ai_agent(k8s_manager):
    return Agent(
        name="Kubernetes AI Assistant",
        role="DevOps Kubernetes Helper",
        goal="Analyze Kubernetes cluster state and give intelligent recommendations.",
        backstory=(
            "You are an expert Kubernetes AI agent. "
            "You read cluster status and provide troubleshooting, optimization tips, "
            "and clear summaries for DevOps engineers."
        ),
        llm=client,
        tools=[k8s_manager],
        verbose=True
    )
