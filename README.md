
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

<img width="1265" height="789" alt="image" src="https://github.com/user-attachments/assets/41af77ee-f000-42e9-98a9-201e77615daa" />

### Nodes Ready

<img width="1045" height="320" alt="image" src="https://github.com/user-attachments/assets/433c883d-d32b-4bc9-9109-12edb7fe2849" />

### NGINX Running

<img width="1035" height="307" alt="Screenshot 2026-05-03 183546" src="https://github.com/user-attachments/assets/690b8e8f-9fee-4198-9ee7-8532ff7ddff8" />


### Application Output

<img width="1907" height="667" alt="image" src="https://github.com/user-attachments/assets/9cfa1222-af72-4c5d-9bc9-4c046994402b" />

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
