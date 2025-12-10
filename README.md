# 🤖 Kubernetes AI Agent using CrewAI, OpenAI & Python

This project builds an **AI-powered Kubernetes Assistant** capable of analyzing cluster state, summarizing workloads, detecting issues, and giving intelligent DevOps recommendations — all through **natural language commands**.

It uses:

- **CrewAI (Agent Framework)**
- **OpenAI LLM**
- **Python**
- **Kubernetes Python Client**
- **Minikube / AWS EC2 / Any K8s Cluster**

This project is perfect for DevOps + AI portfolio building.

---

## 🚀 Features

✔️ Get real-time Kubernetes cluster status  
✔️ List pods, deployments, restarts, nodes  
✔️ Summarize cluster health in natural language  
✔️ Explain issues like a DevOps engineer  
✔️ Give recommendations (scaling, fixes)  
✔️ Works with Minikube, EKS, or any kubeconfig  
✔️ Fully interactive CLI assistant  

---

## 📁 Project Structure

```
k8s-ai-agent/
│
├── agent/
│   ├── __init__.py
│   ├── k8s_agent.py        # Fetches pod/deployment info from Kubernetes
│   ├── ai_agent.py      # AI agent configuration using CrewAI + OpenAI
│
├── config/
│   └── kubeconfig          # Kubernetes cluster authentication (auto generated)
│
├── main.py                 # Chat interface to interact with the AI agent
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash
git https://github.com/Anupj11/K8s_AI_Agent.git
cd k8s-ai-agent
```

---

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set your OpenAI API Key

#### Linux / macOS / WSL:
```bash
export OPENAI_API_KEY="your-api-key"
```

#### Windows:
```powershell
setx OPENAI_API_KEY "your-api-key"
```

---

### 4️⃣ Provide kubeconfig (cluster credentials)

#### For Minikube:
```bash
kubectl config view --raw > config/kubeconfig
```

OR upload any kubeconfig from your Kubernetes cluster (EKS, MicroK8s, Kind, etc.)

---

## ▶️ Running the AI Agent

Start the assistant:

```bash
python main.py
```

You should see:

```
Kubernetes AI Agent Started. Ask anything:
```

---

## 💬 Example Commands

```
Show me all pods
Summarize the cluster health
Why is my deployment failing?
Explain my cluster issues in simple words
Which pods are restarting?
Should I scale my deployment?
```

---

## 🧪 (Optional) Test Deployment

Create a sample app:

```bash
kubectl create deployment nginx --image=nginx
```

Then ask the agent:

```
Is my nginx deployment running correctly?
```

---

## 🛠️ How It Works (Architecture)

1. `k8s_agent.py` connects to Kubernetes using Python client  
2. Fetches pod, deployment, node, and status info  
3. Data is passed to CrewAI + OpenAI agent  
4. Model analyzes cluster state and gives natural-language insights  
5. CLI displays responses interactively  

---

## ⭐ Why This Project Is Valuable for Your Resume

This combines:

- **AI (LLMs + CrewAI)**  
- **DevOps tooling**  
- **Kubernetes automation**  
- **Python backend development**  
- **Cloud testing (AWS EC2)**  

You can proudly add:

> Built an AI-powered Kubernetes operations assistant capable of providing real-time cluster insights, troubleshooting suggestions, and intelligent automation using OpenAI, CrewAI, and Kubernetes Python client.

---

## 🤝 Contributing

Pull requests are welcome.  
Open an issue for feature requests or bugs.

---

## 📜 License

MIT License.

