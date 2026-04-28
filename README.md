# 🚀 End-to-End GitOps DevOps Project

## Overview
This project demonstrates a complete DevOps pipeline using:
- Docker
- Kubernetes (EKS)
- GitHub Actions (CI)
- Argo CD (GitOps CD)
- Prometheus & Grafana (Monitoring)

## Architecture
1. Code pushed to GitHub
2. GitHub Actions builds & pushes Docker image
3. Argo CD syncs Kubernetes manifests
4. App deployed to EKS
5. Prometheus & Grafana monitor system

## Setup Steps

### 1. Build & Push Docker Image
Replace YOUR_DOCKER_USERNAME in k8s/deployment.yaml

### 2. Apply Kubernetes Manifests
kubectl apply -f k8s/

### 3. Setup Argo CD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

### 4. Monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack

## Demo
Scale app:
kubectl scale deployment devops-app --replicas=5

Observe in Grafana dashboards.

## Author

Kalyan M

DevOps Project
