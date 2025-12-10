from crewai import Agent, Tool
from openai import OpenAI
import os

# Import K8sAgent
from agent.k8s_agent import K8sAgent

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
k8s = K8sAgent()

# ---- Tools ----

get_pods_tool = Tool(
    name="Get Kubernetes Pods",
    description="Returns a list of pods and their status.",
    func=lambda _: k8s.get_pods()
)

get_deployments_tool = Tool(
    name="Get Kubernetes Deployments",
    description="Returns deployment objects and their replicas.",
    func=lambda _: k8s.get_deployments()
)

summarize_cluster_tool = Tool(
    name="Summarize Kubernetes Cluster",
    description="Summarizes overall Kubernetes cluster health.",
    func=lambda _: k8s.summarize_cluster()
)

def create_ai_agent():
    return Agent(
        name="Kubernetes AI Assistant",
        role="DevOps Kubernetes Helper",
        goal="Analyze Kubernetes cluster state and give insights and recommendations.",
        backstory=(
            "You are an expert Kubernetes AI agent. "
            "You read cluster state and provide troubleshooting, summaries, and optimization tips "
            "for DevOps engineers."
        ),
        llm=client,
        tools=[
            get_pods_tool,
            get_deployments_tool,
            summarize_cluster_tool
        ],
        verbose=True
    )
