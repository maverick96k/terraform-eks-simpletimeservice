# EKS Terraform Module

This Terraform module provisions an **Amazon Elastic Kubernetes Service (EKS)** cluster along with worker node groups, IAM roles, and required policies.

## Features

- Creates an **EKS Cluster** with configurable Kubernetes version.
- Provisions IAM roles for both the cluster and worker nodes.
- Attaches required AWS-managed IAM policies for EKS and nodes.
- Creates **EKS Managed Node Groups** with configurable:
  - Instance types
  - Capacity type (On-Demand or Spot)
  - Scaling configuration (min, max, desired size)
- Outputs the cluster name and API endpoint.

---

## Module Inputs

| Name | Description | Type | Required |
|------|-------------|------|----------|
| `cluster_name` | Name of the EKS cluster | `string` | ✅ |
| `cluster_version` | Kubernetes version for the cluster | `string` | ✅ |
| `subnet_ids` | List of subnet IDs for EKS and node groups | `list(string)` | ✅ |
| `node_groups` | Map of node group configurations (instance type, scaling, capacity type) | `map(object)` | ✅ |

Example `node_groups` variable structure:
```hcl
node_groups = {
  ng1 = {
    instance_types = ["t3.medium"]
    capacity_type  = "ON_DEMAND"
    scaling_config = {
      desired_size = 2
      max_size     = 3
      min_size     = 1
    }
  }
}
