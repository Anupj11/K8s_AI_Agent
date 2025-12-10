#!/bin/bash

echo "🚀 Starting full setup for Kubernetes AI Agent environment..."

# -------------------------------
# Update System
# -------------------------------
echo "📦 Updating system packages..."
sudo apt update -y && sudo apt upgrade -y

# -------------------------------
# Install Python, pip, and Git
# -------------------------------
echo "🐍 Installing Python, pip, and Git..."
sudo apt install -y python3 python3-pip git

# -------------------------------
# Install Docker
# -------------------------------
echo "🐳 Installing Docker..."
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER

# Reload group permissions
newgrp docker

echo "✔ Docker Installed: $(docker --version)"

# -------------------------------
# Install kubectl
# -------------------------------
echo "⚙ Installing kubectl..."
sudo snap install kubectl --classic

echo "✔ kubectl Installed: $(kubectl version --client --short)"

# -------------------------------
# Install Minikube
# -------------------------------
echo "📦 Installing Minikube..."
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64

echo "✔ Minikube Installed: $(minikube version)"

# -------------------------------
# Start Minikube
# -------------------------------
echo "🚀 Starting Minikube using Docker driver..."
minikube start --driver=docker

echo "✔ Minikube Status:"
minikube status

# -------------------------------
# Verify Docker, kubectl, Minikube
# -------------------------------
echo "🔍 Checking Kubernetes Node..."
kubectl get nodes

echo ""
echo "🎉 SETUP COMPLETE!"
echo "Your system is now ready for:"
echo "➡ Python AI Agent"
echo "➡ Kubernetes development"
echo "➡ Docker workloads"
echo "➡ Minikube testing environment"
echo ""
echo "Next Step: Clone your project repo and run main.py"
