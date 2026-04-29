# 🚀 DevOps CI/CD Pipeline with Jenkins, Docker, AWS ECR & EKS

This project demonstrates a **production-style CI/CD pipeline** built using Jenkins, Docker, AWS ECR, and Kubernetes (EKS).  
It automates the process of building, pushing, and deploying a containerized application.

---

## 📌 Project Overview

The pipeline performs the following steps:

1. Pulls source code from GitHub  
2. Builds a Docker image  
3. Pushes the image to AWS ECR  
4. Updates the Kubernetes deployment on AWS EKS  
5. Ensures automated and repeatable deployments  

---

## 🏗️ Architecture
GitHub → Jenkins → Docker → AWS ECR → AWS EKS → Kubernetes Deployment


---

## 🧰 Tech Stack

- Jenkins (CI/CD automation)
- Docker (Containerization)
- AWS ECR (Container Registry)
- AWS EKS (Kubernetes Cluster)
- Kubernetes (Container Orchestration)
- Node.js (Sample Application)

---

## 📁 Project Structure
├── app.js
├── package.json
├── Dockerfile
├── Jenkinsfile
├── deployment.yaml
├── service.yaml
└── README.md


---

## ⚙️ Prerequisites

Make sure you have the following installed and configured:

- AWS CLI (`aws configure`)
- Docker
- kubectl
- Jenkins (running locally or on server)
- AWS Account with:
  - ECR access
  - EKS cluster

---

## 🔐 Jenkins Setup

### 1. Add AWS Credentials

In Jenkins:

- Go to **Manage Jenkins → Credentials**
- Add:
  - **Kind:** Username with password  
  - **Username:** AWS_ACCESS_KEY_ID  
  - **Password:** AWS_SECRET_ACCESS_KEY  
  - **ID:** `aws-creds`

---

### 2. Required Tools in Jenkins

Ensure Jenkins has access to:

- Docker
- AWS CLI
- kubectl

---

## 🚀 How to Run the Project

### Step 1 — Clone Repository

```bash
git clone https://github.com/<your-username>/devops-project.git
cd devops-project

Step 2 — Create ECR Repository
aws ecr create-repository --repository-name devops-app
Step 3 — Update Configuration

Edit Jenkinsfile and update:

AWS Account ID
ECR Repository URL
Cluster Name (if different)
Step 4 — Deploy Kubernetes Resources
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Step 5 — Run Jenkins Pipeline
Create a Jenkins Pipeline job
Connect GitHub repo
Run Build Now
📊 Verification

Check deployment:

kubectl get pods
kubectl get svc

Access application via LoadBalancer URL.

🔄 CI/CD Flow
Code push → triggers Jenkins pipeline
Jenkins builds Docker image
Image pushed to AWS ECR
Kubernetes deployment updated automatically
⚠️ Important Notes
Ensure IAM user has permissions for:
ECR
EKS
EC2
Ensure your IAM user is mapped in aws-auth configmap
Avoid leaving EKS cluster running to prevent charges

👨‍💻 Author

**Kalyan**
