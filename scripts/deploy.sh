#!/bin/bash
kubectl apply -f logging/loki.yaml
kubectl apply -f logging/promtail.yaml
kubectl apply -f k8s/
