# 🚀 Zomato DevOps Project (End-to-End CI/CD on AWS EKS)

## 📌 Project Overview

This project demonstrates a complete DevOps pipeline to deploy a food delivery application using modern cloud-native tools.

The pipeline automates the process from **code commit → build → containerization → deployment → monitoring** with zero manual intervention.

---

## 🏗️ Architecture Flow

Developer → GitHub → Jenkins → Docker → AWS ECR → AWS EKS → Users
Monitoring → Prometheus + Grafana

---

## 🛠️ Tech Stack

* AWS (EC2, ECR, EKS)
* Jenkins (CI/CD)
* Docker (Containerization)
* Kubernetes (Orchestration)
* Prometheus (Monitoring)
* Grafana (Visualization)

---

# ⚙️ Step-by-Step Setup Guide

---

## 🔹 Step 1: Launch EC2 Instance (Jenkins Server)

* OS: Ubuntu 22.04
* Instance Type: t2.medium (or higher)
* Open Ports:

  * 22 (SSH)
  * 8080 (Jenkins)
  * 80 (HTTP)

### Connect to EC2

```bash
ssh ubuntu@<your-ec2-ip>
```

---

## 🔹 Step 2: Install Required Tools

```bash
sudo apt update -y
sudo apt install -y openjdk-17-jdk docker.io git
```

### Start Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Give Docker Permission

```bash
sudo usermod -aG docker ubuntu
```

---

## 🔹 Step 3: Install Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
/usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install jenkins -y
```

### Start Jenkins

```bash
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

### Access Jenkins

```
http://<EC2-IP>:8080
```

---

## 🔹 Step 4: Create AWS ECR Repository

1. Go to AWS Console → ECR
2. Click "Create Repository"
3. Name: `zomato-foodapp`

Copy the repository URI:

```
<your-ecr-uri>
```

---

## 🔹 Step 5: Setup AWS CLI

```bash
sudo apt install awscli -y
aws configure
```

Enter:

* Access Key
* Secret Key
* Region: ap-south-1


## 🔹 Step 6: Setup EKS Cluster

### Install eksctl

```bash
curl -sLO https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz
tar -xzf eksctl_Linux_amd64.tar.gz
sudo mv eksctl /usr/local/bin
```

### Create Cluster

```bash
eksctl create cluster \
--name zomato-cluster \
--region ap-south-1 \
--node-type t3.medium \
--nodes 2
```

### Verify
```

---

## 🔹 Step 7: Update Project Files

Replace this in files:
* `jenkins/Jenkinsfile`
* `kubernetes/deployment.yaml`

### Replace:

```
<your-ecr-uri>
```

with:

```
your actual ECR URI
```

---

## 🔹 Step 8: Configure Jenkins Pipeline

### Install Plugins:

* Docker Pipeline
* Kubernetes CLI
* Git
* Pipeline

---

### Create New Pipeline Job

1. Open Jenkins
2. Click **New Item**
3. Select **Pipeline**
4. Scroll → Pipeline script from SCM
5. Add Git repo:

```
https://github.com/staragile2016/FoodAppZomato.git
```

---

## 🔹 Step 9: Setup GitHub Webhook

1. Go to GitHub repo
2. Settings → Webhooks
3. Add webhook:

```
http://<EC2-IP>:8080/github-webhook/
```

---

## 🔹 Step 10: Run Pipeline

* Push code to GitHub
* Jenkins will trigger automatically
* Pipeline will:

  * Build app
  * Create Docker image
  * Push to ECR
  * Deploy to EKS

---

## ☸️ Step 11: Deploy Kubernetes Resources

```bash
kubectl apply -f kubernetes/
```

---

## 📈 Step 12: Enable Auto Scaling

```bash
kubectl apply -f kubernetes/hpa.yaml
```

---

## 📊 Step 13: Setup Monitoring

### Install Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Add Repo

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### Install Monitoring Stack

```bash
helm install prometheus prometheus-community/kube-prometheus-stack
```

---

## 🔹 Access Grafana

```bash
kubectl port-forward svc/prometheus-grafana 3001:80 --address 0.0.0.0
```

Open:

```
http://<EC2-IP>:3001
```

Default:

* Username: admin
* Password: prom-operator

---

## 🔄 Step 14: Rollback Strategy

```bash
kubectl rollout undo deployment/zomato-deployment
```

---

## 🎯 Final Outcome

✅ Fully automated CI/CD pipeline
✅ Zero manual deployment
✅ Scalable Kubernetes deployment
✅ Auto-scaling enabled
✅ Monitoring with Grafana
✅ Production-ready architecture

---

Built an end-to-end DevOps pipeline using Jenkins, Docker, and Kubernetes (EKS) on AWS with automated CI/CD, auto-scaling, and monitoring using Prometheus and Grafana.

---

### Files:


```bash
kubectl get nodes

