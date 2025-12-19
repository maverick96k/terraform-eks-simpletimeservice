# SimpleTimeService – Terraform (VPC + EKS) + Kubernetes Deployment

This project provisions AWS infrastructure using Terraform (VPC + EKS) and deploys a sample microservice (`simpletimeservice`) to the cluster.

---

## 1. Install Required Tools

Ensure the following tools are installed and available in your PATH:

### Required CLI utilities
- **AWS CLI v2**  
  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

- **Terraform**  
  https://developer.hashicorp.com/terraform/downloads

- **kubectl**  
  https://kubernetes.io/docs/tasks/tools/

- **eksctl**  
  https://eksctl.io/introduction/installation/

### Verify installation:
```bash
aws --version
terraform version
kubectl version --client
eksctl version
```

---

## 2. Create AWS Infrastructure with Terraform

Initialize Terraform in the main project directory:

```bash
cd terraform
terraform init
```

Review changes before applying:

```bash
terraform plan -out tfplan
```

Create the VPC + EKS cluster:

```bash
terraform apply "tfplan"
```

Terraform will:
- Create a VPC with public + private subnets
- Create an EKS cluster
- Create worker node groups in private subnets

---

## 3. Configure kubeconfig (Cluster Access)

Once Terraform completes, generate kubeconfig using eksctl:

```bash
eksctl utils write-kubeconfig \
  --cluster <cluster-name> \
  --region <aws-region>
```

Example:

```bash
eksctl utils write-kubeconfig --cluster simpletimeservice-eks --region us-east-1
```

Verify that kubectl can access the cluster:

```bash
kubectl get nodes
kubectl get pods -A
```

---

## 4. Deploy Kubernetes Manifests

After kubeconfig is configured, apply the workload:

```bash
kubectl apply -f k8s-manifests.yaml
```

Verify Deployment, Service, and (optional) LoadBalancer:

```bash
kubectl get all -n simpletimeservice
```

If using a LoadBalancer service, get the external URL:

```bash
kubectl get svc -n simpletimeservice
```

---

## Cleanup

To destroy all resources:

```bash
terraform destroy
```

---

## Notes

- The EKS worker nodes run in private subnets.
- LoadBalancer services require properly tagged public subnets.
- Ensure AWS credentials are configured before running Terraform or eksctl:
```bash
aws configure
```

