from kubernetes import client, config
import datetime

class K8sAgent:
    def __init__(self, kubeconfig_path="config/kubeconfig"):
        config.load_kube_config(kubeconfig_path)
        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()

    def get_pods(self, namespace="default"):
        pods = self.core.list_namespaced_pod(namespace)
        pod_list = []
        for pod in pods.items:
            pod_list.append({
                "name": pod.metadata.name,
                "status": pod.status.phase,
                "node": pod.spec.node_name,
                "restarts": pod.status.container_statuses[0].restart_count
            })
        return pod_list

    def get_deployments(self, namespace="default"):
        deployments = self.apps.list_namespaced_deployment(namespace)
        deploy_list = []
        for dep in deployments.items:
            deploy_list.append({
                "name": dep.metadata.name,
                "replicas": dep.status.replicas,
                "available": dep.status.available_replicas,
            })
        return deploy_list

    def summarize_cluster(self):
        pods = self.get_pods()
        deployments = self.get_deployments()

        summary = f"Cluster Summary ({datetime.datetime.now()}):\n\n"
        summary += f"Pods: {len(pods)}\n"
        for p in pods:
            summary += f"- {p['name']} (Status: {p['status']}, Restarts: {p['restarts']})\n"

        summary += f"\nDeployments: {len(deployments)}\n"
        for d in deployments:
            summary += f"- {d['name']} (Replicas: {d['replicas']}, Available: {d['available']})\n"

        return summary
