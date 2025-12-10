import os
import json
import requests
from agent.k8s_agent import K8sAgent

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

k8s = K8sAgent("config/kubeconfig")

def ask_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",   # required
        "X-Title": "K8s AI Agent"
    }

    body = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=body)
    
    if response.status_code != 200:
        return f"❌ LLM Error {response.status_code}: {response.text}"
    
    return response.json()["choices"][0]["message"]["content"]


def handle_query(query: str):
    q = query.lower()

    if "pod" in q:
        pods = k8s.get_pods()
        prompt = f"""
User Query: {query}

Kubernetes Pods:
{json.dumps(pods, indent=2)}

Explain pod status, errors, and recommended fixes.
"""
        return ask_llm(prompt)

    if "deployment" in q:
        deps = k8s.get_deployments()
        prompt = f"""
User Query: {query}

Deployments:
{json.dumps(deps, indent=2)}

Summarize health and suggest improvements.
"""
        return ask_llm(prompt)

    if "cluster" in q or "summary" in q:
        summary = k8s.summarize_cluster()
        prompt = f"""
User Query: {query}

Cluster Summary:
{summary}

Rewrite it in a professional DevOps format.
"""
        return ask_llm(prompt)

    # fallback
    pods = k8s.get_pods()
    prompt = f"""
User Query: {query}

Pod Snapshot:
{json.dumps(pods, indent=2)}

Provide a helpful Kubernetes explanation.
"""
    return ask_llm(prompt)
