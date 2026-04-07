# 🚀 DevOps Flask Portfolio App

A production-ready **2-tier web application** built with **Flask + MySQL**, containerized using **Docker**, and deployed on **AWS EC2** with **Nginx reverse proxy**.

---

## 📌 Project Overview

This project demonstrates a complete **DevOps workflow**:

* Backend: Flask (Python)
* Database: MySQL
* Containerization: Docker & Docker Compose
* Deployment: AWS EC2
* Reverse Proxy: Nginx
* CI/CD (optional): Jenkins

---

## 🏗️ Architecture

```
User → Browser → Nginx → Flask App → MySQL Database
```

---

## ✨ Features

* 💬 Submit messages via web UI
* 🗄️ Store messages in MySQL database
* 📜 Display stored messages dynamically
* 🐳 Fully Dockerized application
* ☁️ Deployable on AWS EC2
* 🔁 Restart-safe with persistent volumes

---

## 🛠️ Tech Stack

* Python (Flask)
* MySQL
* Docker & Docker Compose
* AWS EC2
* Nginx

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── templates/
    └── index.html
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/devops-flask-portfolio-app.git
cd devops-flask-portfolio-app
```

---

### 2️⃣ Configure Environment Variables

Create `.env` file:

```
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=devops
MYSQL_USER=devuser
MYSQL_PASSWORD=devpass
MYSQL_HOST=mysql
MYSQL_DB=devops
```

---

### 3️⃣ Run Application (Docker)

```
docker compose up -d --build
```

---

### 4️⃣ Access Application

```
http://<EC2-PUBLIC-IP>:5000
```

---

## 🌐 Nginx Setup (Optional)

Configure reverse proxy:


```
server {
    listen 80;

    location / {
        proxy_pass http://localhost:5000;
    }
}
```

Then restart Nginx:


```
sudo systemctl restart nginx
```

Access app:

```
http://<EC2-IP>
```

---

## 🔍 Troubleshooting

### Check running containers

```
docker ps
```

### View logs

```
docker logs flask-app
docker logs mysql
```

### Restart services

```
docker compose down -v
docker compose up -d --build
```

---

## 🚀 Future Improvements

* 🔐 Add authentication system
* 🌍 Custom domain with HTTPS
* ⚙️ CI/CD pipeline using Jenkins/GitHub Actions
* ☸️ Kubernetes (EKS) deployment
* 📊 Monitoring with Prometheus & Grafana

---

## 👨‍💻 Author

**Kalyan**

* GitHub: https://github.com/Saviperr

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

