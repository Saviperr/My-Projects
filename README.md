# ☁️ AWS 3-Tier Architecture Project

## 📌 Project Overview

This project demonstrates the deployment of a **3-tier web application architecture on AWS** using core cloud services.
It follows a traditional manual setup approach without DevOps tools, focusing on strong fundamentals of networking and infrastructure.

---

## 🏗️ Architecture

Frontend → Backend → Database

* **S3** → Static Website Hosting (Frontend)
* **EC2** → Node.js Application (Backend API)
* **RDS MySQL** → Database (Private Subnet)

---

## ⚙️ Tech Stack

* AWS S3 (Frontend Hosting)
* AWS EC2 (Backend Server)
* AWS RDS (MySQL Database)
* AWS VPC (Networking)
* Node.js (Backend)
* HTML/JS (Frontend)

---

## 🚀 Key Features

* 3-tier architecture (presentation, application, database)
* Secure VPC with public & private subnets
* RDS deployed in private subnet (no public access)
* Secure communication using Security Groups
* End-to-end data flow from frontend to database
* Manual deployment (no automation tools)

---

## 🛠️ Step-by-Step Setup

### 1. Create VPC

* CIDR: 10.0.0.0/16
* Create public & private subnets

---

### 2. Setup Internet Gateway & Route Table

* Attach IGW to VPC
* Add route `0.0.0.0/0` to public subnet

---

### 3. Configure Security Groups

**EC2 SG**

* SSH (22) → My IP
* HTTP (80) → 0.0.0.0/0

**RDS SG**

* MySQL (3306) → EC2 SG

---

### 4. Launch EC2 (Backend)

* Ubuntu 22.04
* Install Node.js & MySQL client

```bash
sudo apt update
sudo apt install nodejs npm mysql-client -y
```

---

### 5. Setup Backend Application

* Create Node.js app (`server.js`)
* Connect to RDS database

⚠️ Update:

```js
host: "RDS-ENDPOINT"
```

---

### 6. Create RDS Database

* Engine: MySQL
* Instance: db.t3.micro
* Private subnet (no public access)

---

### 7. Create Table

```sql
CREATE DATABASE userdata;
USE userdata;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100)
);
```

---

### 8. Start Backend

```bash
sudo node server.js
```

---

### 9. Setup Frontend (S3)

* Upload `index.html`
* Enable static website hosting

⚠️ Update:

```js
http://EC2_PUBLIC_IP/submit-data
```

---

### 10. Bucket Policy

Allow public read access for S3 objects.

---

### 11. Test Application

# ☁️ AWS 3-Tier Architecture Project

## 📌 Project Overview

This project demonstrates the deployment of a **3-tier web application architecture on AWS** using core cloud services.
It follows a traditional manual setup approach without DevOps tools, focusing on strong fundamentals of networking and infrastructure.

---

## 🏗️ Architecture

Frontend → Backend → Database

* **S3** → Static Website Hosting (Frontend)
* **EC2** → Node.js Application (Backend API)
* **RDS MySQL** → Database (Private Subnet)

---

## ⚙️ Tech Stack

* AWS S3 (Frontend Hosting)
* AWS EC2 (Backend Server)
* AWS RDS (MySQL Database)
* AWS VPC (Networking)
* Node.js (Backend)
* HTML/JS (Frontend)

---

## 🚀 Key Features

* 3-tier architecture (presentation, application, database)
* Secure VPC with public & private subnets
* RDS deployed in private subnet (no public access)
* Secure communication using Security Groups
* End-to-end data flow from frontend to database
* Manual deployment (no automation tools)

---

## 🛠️ Step-by-Step Setup

### 1. Create VPC

* CIDR: 10.0.0.0/16
* Create public & private subnets

---

### 2. Setup Internet Gateway & Route Table
* Attach IGW to VPC
* Add route `0.0.0.0/0` to public subnet

---

### 3. Configure Security Groups

**EC2 SG**

**RDS SG**


### 4. Launch EC2 (Backend)

* Ubuntu 22.04
* Install Node.js & MySQL client

```bash
sudo apt update
sudo apt install nodejs npm mysql-client -y
* MySQL (3306) → EC2 SG

```

---

### 5. Setup Backend Application

* Create Node.js app (`server.js`)
* Connect to RDS database

⚠️ Update:

```js
host: "RDS-ENDPOINT"
```

---

### 6. Create RDS Database

* Engine: MySQL
* Instance: db.t3.micro
* Private subnet (no public access)

---

### 7. Create Table

```sql
CREATE DATABASE userdata;
USE userdata;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100)
);
```

---

### 8. Start Backend

```bash
sudo node server.js
```

---

### 9. Setup Frontend (S3)

* Upload `index.html`
* Enable static website hosting

⚠️ Update:

```js
http://EC2_PUBLIC_IP/submit-data
```

---

### 10. Bucket Policy

Allow public read access for S3 objects.

---

### 11. Test Application

Flow:
User → S3 → EC2 → RDS

Verify:

```sql
SELECT * FROM users;
```

---

## 🔄 Optional: Route53

* Configure domain
* Point to S3 website endpoint

---

## 🎯 Final Outcome

* Fully functional 3-tier architecture
* Secure networking using VPC
* Data stored in RDS via backend API
* Frontend hosted on S3
* Production-style cloud setup

---
Built a 3-tier web application architecture on AWS using **S3 (frontend), EC2 (backend), and RDS (database)** with secure VPC networking.
Implemented end-to-end data flow from user interface to database with proper security groups and private subnet configuration.

---
---
* SSH (22) → My IP
* HTTP (80) → 0.0.0.0/0


