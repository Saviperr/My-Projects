#!/bin/bash

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz"
tar -xzf eksctl_Linux_amd64.tar.gz
sudo mv eksctl /usr/local/bin

eksctl create cluster     --name zomato-cluster     --region ap-south-1     --node-type t3.medium     --nodes 2

kubectl get nodes