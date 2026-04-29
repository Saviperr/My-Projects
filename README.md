# DevOps CI/CD Pipeline Project

This project demonstrates a complete CI/CD pipeline using:
- Jenkins
- Docker
- AWS ECR
- AWS EKS
- Kubernetes

## Steps to Run

1. Build Docker Image
2. Push to AWS ECR
3. Deploy to Kubernetes (EKS)
4. Jenkins automates the full pipeline

## Requirements

- AWS CLI configured
- Docker installed
- kubectl installed
- Jenkins setup with credentials

## Run Kubernetes Deployment

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Author

Kalyan
