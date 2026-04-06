# Zomato DevOps Project

End-to-End CI/CD pipeline using AWS, Docker, Kubernetes, Jenkins.

## Steps
1. Setup Jenkins using scripts/setup-jenkins.sh
2. Setup EKS using scripts/eks-setup.sh
3. Update ECR URI in Jenkinsfile & deployment.yaml
4. Run Jenkins pipeline

## Features
- CI/CD Automation
- Docker containerization
- Kubernetes deployment
- Auto Scaling
- Monitoring ready

## Note
Replace <your-ecr-uri> before running