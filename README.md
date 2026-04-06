# 🎬 BookMyShow DevOps Project (CI/CD on AWS EKS)

## 📌 Overview

This project demonstrates an end-to-end DevOps pipeline for deploying a movie ticket booking application using AWS, Docker, Kubernetes, and Jenkins.

---

## 🏗 Architecture

GitHub → Jenkins → Docker → AWS ECR → AWS EKS → Users
Monitoring → Prometheus + Grafana

---

## 🛠️ Tech Stack

* AWS (EC2, ECR, EKS)
* Jenkins
* Docker
* Kubernetes
* Prometheus & Grafana

---

## 🚀 Setup Steps

### 1. Launch EC2 (Jenkins Server)

* Ubuntu 22.04
* Open ports: 22, 8080

### 2. Install Tools

```bash
sudo apt update
sudo apt install -y openjdk-17-jdk docker.io git awscli
```

### 3. Install Jenkins

```bash
sudo apt install jenkins -y
sudo systemctl start jenkins
```

### 4. Setup EKS

```bash
eksctl create cluster --name bms-cluster --region ap-south-1 --nodes 2
```

### 5. Create ECR Repo

* Name: bms-app
* Copy URI

---

## ⚠️ IMPORTANT

Replace:

```
<your-ecr-uri>
```

In:

* Jenkinsfile
* deployment.yaml

---

## 🚀 Deployment

```bash
kubectl apply -f kubernetes/
```

---

## 📊 Monitoring

```bash
helm install monitoring prometheus-community/kube-prometheus-stack
```

---

## 🔄 Rollback

```bash
kubectl rollout undo deployment bms-deployment
```

---

## 🎯 Outcome

* CI/CD automated
* Scalable deployment
* Load-balanced app
* Monitoring enabled

---
Deployed a scalable ticketing platform using Jenkins, Docker, and Kubernetes (EKS) with automated CI/CD and monitoring.
