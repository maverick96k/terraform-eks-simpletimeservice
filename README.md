# SimpleTimeService – Application + AWS EKS Infrastructure

This repository contains two components:

1. **SimpleTimeService (app/)**  
   A minimal HTTP microservice that returns the current timestamp and the client's IP address.

2. **Infrastructure (terraform/)**  
   Terraform configurations that provision an AWS VPC and EKS cluster, and the Kubernetes manifests that deploy the application.

This project demonstrates a full end-to-end workflow:
Build → Containerize → Deploy on AWS EKS using Terraform → Expose via LoadBalancer.

---

## 📁 Repository Structure

```
.
├── app/                     # SimpleTimeService source code (Python/Docker)
│   ├── app.py
│   ├── Dockerfile
│   ├── README.md
│
│
└── terraform/               # Complete AWS infrastructure-as-code
    ├── Modules/
    │   ├── vpc/             # VPC module
    │   └── eks/             # EKS module
    ├── k8s-manifests.yaml   # Kubernetes Deployment & Service
    ├── main.tf              # Terraform orchestration
    ├── variables.tf
    ├── outputs.tf
    └── README.md            # Terraform-specific instructions
```

---

## 🚀 Application: SimpleTimeService (app/)

A minimal web server that returns JSON:

```json
{
  "timestamp": "<current UTC time>",
  "ip": "<client IP>"
}
```

### Run locally (Docker):

```bash
cd app
docker build -t simpletimeservice:latest .
docker run --rm -p 8080:8080 simpletimeservice:latest
```

### Test:

```bash
curl http://localhost:8080/
```

### Public Image:

```
maverick96k/simpletimeservice:latest
```

---

## ☁️ Infrastructure: AWS VPC + EKS (terraform/)

The Terraform configuration provisions:

- A VPC with public + private subnets  
- An EKS cluster running Kubernetes  
- Managed worker node groups in **private subnets**  
- A LoadBalancer to expose the service  
- Kubernetes namespace, Deployment, and Service

---

## 🔧 Prerequisites

You must install:

```
aws CLI
terraform
kubectl
eksctl
docker
```

Verify:

```bash
aws --version
terraform version
kubectl version --client
eksctl version
docker --version
```

Configure AWS credentials:

```bash
aws configure
```

---

## 🏗️ 1. Provision Infrastructure

From the `terraform/` directory:

```bash
terraform init
terraform plan
terraform apply -auto-approve
```
