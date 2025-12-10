import os
import json
from openai import OpenAI
from agent.k8s_agent import K8sAgent

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
k8s = K8sAgent("config/kubeconfig")


# -------- LLM Call --------

def ask_llm(prompt: str):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    try:
        # New Responses API — Most correct output
        return response.output_text
    except:
        # Fallback for older formats
        try:
            return response.output[0].content[0].text
        except:
            return str(response)


# -------- Query Handler --------

def handle_query(query: str):
    q = query.lower()

    # GET PODS
    if "pod" in q:
        pods = k8s.get_pods()
        prompt = f"""
User Query: {query}

Pods Data:
{json.dumps(pods, indent=2)}

Provide:
1. Pod summary
2. Any unhealthy pods
3. Possible reasons
4. Recommended fix
"""
        return ask_llm(prompt)

    # GET DEPLOYMENTS
    if "deployment" in q:
        deps = k8s.get_deployments()
        prompt = f"""
User Query: {query}

Deployments Data:
{json.dumps(deps, indent=2)}

Provide:
1. Deployment summary
2. Missing replicas issues
3. Suggestions
"""
        return ask_llm(prompt)

    # CLUSTER SUMMARY
    if "cluster" in q or "summary" in q:
        summary = k8s.summarize_cluster()
        prompt = f"""
User Query: {query}

Cluster Raw Summary:
{summary}

Rewrite into a clean, readable, 6-line summary with recommendations.
"""
        return ask_llm(prompt)

    # DEFAULT FALLBACK
    pods = k8s.get_pods()
    prompt = f"""
User Query: {query}

Pods Snapshot:
{json.dumps(pods, indent=2)}

Provide a helpful Kubernetes answer with suggestions.
"""
    return ask_llm(prompt)
