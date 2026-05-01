# 🚀 KubeInsight

## 👨‍💻 Built by Kalyan

---

## 🧠 What is this?

I built this project to understand how **logging actually works in a real Kubernetes setup**.

Instead of just learning theory, I wanted to:

* collect logs from running pods
* send them somewhere centralized
* and actually see them in a dashboard

So this project is basically my hands-on implementation of a **Kubernetes logging pipeline using Loki + Promtail + Grafana**.

---

## ⚙️ What it does

* Runs a sample app that keeps generating logs
* Promtail collects logs from all pods
* Loki stores those logs
* Grafana lets you query and visualize them

Simple idea, but setting it up properly took a lot of debugging 😄

---

## 🏗️ How it works (in simple terms)

```
Pods → Promtail → Loki → Grafana
```

* Pods generate logs
* Promtail reads logs from the node
* Sends them to Loki
* Grafana queries Loki

---

## 📁 Project Structure

```
kubeinsight/
│
├── k8s/            # sample app (log generator)
├── logging/        # loki + promtail configs
├── monitoring/     # grafana datasource
├── scripts/        # deploy & cleanup
└── README.md
```

---

## 🚀 How to run this

### 1. Clone the repo

```bash
git clone https://github.com/your-username/kubeinsight.git
cd kubeinsight
```

---

### 2. Deploy everything

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

This will:

* start Loki
* start Promtail
* start a sample app that generates logs

---

### 3. Check if things are running

```bash
kubectl get pods -n logging
kubectl get pods
```

---

### 4. Connect Grafana to Loki

In Grafana:

* Go to **Data Sources**
* Add **Loki**
* Use this URL:

```
http://loki.logging.svc.cluster.local:3100
```

---

### 5. See logs

Go to **Explore → Loki**

Run:

```
{}
```

Set time range to last 1 hour

You should see logs like:

```
HELLO_KALYAN_LOG
```

---

## 🧪 Why I made this

Honestly, I struggled a lot with:

* Loki configs
* Helm issues
* pods stuck in Pending
* weird 500 errors
* storage problems

So instead of just giving up, I kept debugging until I understood:

👉 how logging actually works in Kubernetes

This project is the result of that process.

---

## 💡 What I learned

* "Running" doesn’t mean "Ready" in Kubernetes
* Logging systems fail silently if misconfigured
* Loki configs are tricky (especially replication + storage)
* Promtail needs correct service discovery
* Debugging is the real skill in DevOps

---

## 🚧 What I can add next

# 🚀 KubeInsight

## 👨‍💻 Built by Kalyan

---

## 🧠 What is this?

I built this project to understand how **logging actually works in a real Kubernetes setup**.

Instead of just learning theory, I wanted to:

* collect logs from running pods
* send them somewhere centralized
* and actually see them in a dashboard

So this project is basically my hands-on implementation of a **Kubernetes logging pipeline using Loki + Promtail + Grafana**.

---

## ⚙️ What it does

* Runs a sample app that keeps generating logs
* Promtail collects logs from all pods
* Loki stores those logs
* Grafana lets you query and visualize them

Simple idea, but setting it up properly took a lot of debugging 😄

---

## 🏗️ How it works (in simple terms)

```
Pods → Promtail → Loki → Grafana
```

* Pods generate logs
* Promtail reads logs from the node
* Sends them to Loki
* Grafana queries Loki

---
## 📁 Project Structure

```
├── logging/        # loki + promtail configs
├── monitoring/     # grafana datasource
├── scripts/        # deploy & cleanup
---

## 🚀 How to run this

### 1. Clone the repo

```bash
git clone https://github.com/your-username/kubeinsight.git
cd kubeinsight
```
### 2. Deploy everything

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

This will:

* start Loki
---

### 3. Check if things are running

```bash
kubectl get pods -n logging
kubectl get pods
```
### 4. Connect Grafana to Loki

In Grafana:

* Go to **Data Sources**
* Add **Loki**
* Use this URL:
```

---

### 5. See logs

Go to **Explore → Loki**

Run:

```
{}
```

Set time range to last 1 hour

You should see logs like:

```
HELLO_KALYAN_LOG
```

---

## 🧪 Why I made this

Honestly, I struggled a lot with:

* Loki configs
* Helm issues
* pods stuck in Pending
* weird 500 errors
* storage problems

So instead of just giving up, I kept debugging until I understood:

👉 how logging actually works in Kubernetes

This project is the result of that process.

---

## 💡 What I learned

* "Running" doesn’t mean "Ready" in Kubernetes
* Logging systems fail silently if misconfigured
* Loki configs are tricky (especially replication + storage)
* Promtail needs correct service discovery
* Debugging is the real skill in DevOps

---

## 🚧 What I can add next

* Prometheus (metrics)
* Jaeger (tracing)
* CI/CD pipeline
* Terraform setup

---

## 🎯 Final thoughts

This isn’t just a project — it’s something I built while figuring things out the hard way.

If you're learning DevOps or Kubernetes logging, this setup will save you a lot of time.

---

⭐ If this helped you, feel free to star the repo

```
http://loki.logging.svc.cluster.local:3100

---

* start Promtail
* start a sample app that generates logs


---

└── README.md
```

kubeinsight/
│
├── k8s/            # sample app (log generator)

