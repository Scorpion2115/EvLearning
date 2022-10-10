# Deploy EC2 using Terraform
## Reference
* [Terraform | VPC, Subnets, EC2, and more](https://sammeechward.com/terraform-vpc-subnets-ec2-and-more/)

## Introduction
Terraform is an open-source infrastructure as code software tool that let’s us configure our infrastructure using declarative configuration files.

In this lab, we will take a look at how to do the following using terraform:

* Create a VPC and subnets
* Create an internet gateway and route table to make the subnet public
* Create security groups
* Create an ec2 instance on a public subnet and install nginx


1. Create a VPC
2. Create subnets for different parts of the infrastructure
3. Attached an internet gateway to the VPC
4. Create a route table for a public subnet
5. Create security group to allow specific traffic
6. Create EC2 instances within the subnets.
To setup a new ssh key for this instance, run the following command using the aws cli.
```bash
sudo aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > ~/.ssh/MyKeyPair.pem
sudo chmod 400  ~/.ssh/MyKeyPair.pem
```