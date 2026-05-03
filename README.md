
# 🚀 Scalable Infrastructure on AWS EKS using Terraform

![AWS](https://img.shields.io/badge/AWS-EKS-orange)
![Terraform](https://img.shields.io/badge/IaC-Terraform-blue)
![Kubernetes](https://img.shields.io/badge/Orchestration-Kubernetes-blue)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)

---

## 👨‍💻 Author

**Kalyan**

---

## 📌 Project Overview

This project demonstrates how to provision scalable infrastructure on AWS using Terraform and deploy a containerized application using Kubernetes (EKS) with Ingress.

---

## 🧱 Architecture

```
User → AWS Load Balancer → Ingress → Kubernetes Service → Pods (NGINX)
```

---

## 🛠️ Tech Stack

* Terraform (Infrastructure as Code)
* AWS EKS (Managed Kubernetes)
* Kubernetes (Deployment & Services)
* NGINX (Sample Application)
* Ingress Controller (Routing)

---

## ⚙️ Infrastructure Setup

### 1️⃣ Initialize Terraform

```bash
terraform init
```

### 2️⃣ Apply Infrastructure

```bash
terraform apply -auto-approve
```

### 3️⃣ Configure kubectl

```bash
aws eks update-kubeconfig --region ap-south-1 --name my-eks
```

---

## 🚀 Application Deployment

```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --type=LoadBalancer --port=80
```

---

## 🌐 Ingress Setup

```bash
kubectl apply -f k8s/ingress.yaml
```

---

## 📸 Screenshots

### EKS Cluster

![Cluster](screenshots/eks-cluster.png)

### Nodes Ready

![Nodes](screenshots/kubectl-nodes.png)

### NGINX Running

![Pods](screenshots/nginx-output.png)

### Application Output

![Output](screenshots/ingress-output.png)

---

## 💡 Key Learnings

* Built scalable infrastructure using Terraform
* Deployed Kubernetes cluster on AWS EKS
* Managed deployments using kubectl
* Implemented Ingress for routing traffic
* Troubleshot real-world issues (IAM, AMI, provider versions)

---

## 🧹 Cleanup

```bash
terraform destroy -auto-approve
```

---

## ⭐ Why this project stands out

* End-to-end DevOps pipeline (Infra → Deploy → Access)
* Real cloud environment (AWS)
* Production-style architecture
* Hands-on troubleshooting experience

---
