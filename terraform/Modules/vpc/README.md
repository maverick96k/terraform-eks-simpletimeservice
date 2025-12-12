# VPC Terraform Module

This Terraform module provisions an **AWS Virtual Private Cloud (VPC)** with **public and private subnets**, internet gateway, NAT gateways, and route tables.  
It is designed to be used as part of an EKS or general AWS infrastructure deployment.

## Features

- Creates a VPC with DNS support and hostnames enabled.
- Provisions **public and private subnets** across multiple Availability Zones.
- Deploys an **Internet Gateway** for public subnets.
- Allocates **Elastic IPs** for NAT Gateways.
- Deploys **NAT Gateways** for outbound internet access from private subnets.
- Creates and associates **Route Tables** for both public and private subnets.
- Includes proper tagging for Kubernetes/EKS integration.

---

## Module Inputs

| Name | Description | Type | Required |
|------|-------------|------|----------|
| `vpc_cidr` | CIDR block for the VPC | `string` | ✅ |
| `availability_zones` | List of Availability Zones to use | `list(string)` | ✅ |
| `private_subnet_cidrs` | List of CIDR blocks for private subnets | `list(string)` | ✅ |
| `public_subnet_cidrs` | List of CIDR blocks for public subnets | `list(string)` | ✅ |
| `cluster_name` | Name of the EKS cluster (used for tagging) | `string` | ✅ |

---

## Module Outputs

| Name | Description |
|------|-------------|
| `vpc_id` | ID of the created VPC |
| `private_subnet_ids` | IDs of the created private subnets |
| `public_subnet_ids` | IDs of the created public subnets |

---

## Example Usage

```hcl
module "networking" {
  source = "git::https://github.com/<org>/infra-modules.git//networking/vpc?ref=v1.0.0"

  vpc_cidr             = "10.0.0.0/16"
  availability_zones   = ["us-east-1a", "us-east-1b", "us-east-1c"]

  private_subnet_cidrs = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]

  public_subnet_cidrs = [
    "10.0.101.0/24",
    "10.0.102.0/24",
    "10.0.103.0/24"
  ]

  cluster_name = "my-eks-cluster"
}
