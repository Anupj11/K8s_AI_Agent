#!/bin/bash

set -e

echo "🚀 Starting full setup for Kubernetes AI Agent environment..."

# -------------------------------
# Update System
# -------------------------------
echo "📦 Updating and upgrading system packages..."
sudo apt update -y
sudo apt upgrade -y

# -------------------------------
# Install Python3, pip, Git, curl, apt-transport-https, ca-certificates
# -------------------------------
echo "🐍 Installing Python3, pip, Git, curl and dependencies..."
sudo apt install -y python3 python3-pip git curl apt-transport-https ca-certificates gnupg lsb-release

# -------------------------------
# Install Docker
# -------------------------------
echo "🐳 Installing Docker..."
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER

# newgrp docker is tricky — skip for script
echo "✔ Docker version: $(docker --version)"

# -------------------------------
# Install kubectl (official stable release)
# -------------------------------
echo "⚙ Installing kubectl..."
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
rm kubectl
echo "✔ kubectl version: $(kubectl version --client --short)"

# -------------------------------
# Install Minikube (official)
# -------------------------------
echo "📦 Installing Minikube..."
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64
echo "✔ Minikube version: $(minikube version)"

# -------------------------------
# Start Minikube using Docker driver
# -------------------------------
echo "🚀 Starting Minikube with Docker driver..."
minikube start --driver=docker
echo "✔ Minikube status:"
minikube status

# -------------------------------
# Verify Kubernetes Nodes
# -------------------------------
echo "🔍 Verifying Kubernetes cluster nodes..."
kubectl get nodes

echo ""
echo "🎉 SETUP COMPLETE!"
echo "Your system is ready for:"
echo "→ Python AI Agent"
echo "→ Kubernetes (Minikube) development"
echo "→ Docker workloads"
echo ""
echo "Next Step: Clone your project repo and run main.py"
