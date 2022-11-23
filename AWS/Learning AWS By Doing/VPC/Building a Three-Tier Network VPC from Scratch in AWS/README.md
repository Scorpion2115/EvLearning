# Building a Three-Tier Network VPC from scratch
## Introduction
This lab provides you with the opportunity to get hands-on experience building and connecting the following components inside AWS:

- VPC
- Subnets
- Internet Gateway
- Route Tables
- Nat Gateway
- Network Access Control Lists (NACLs)
These components are the foundation of highly available/fault tolerant networking architecture inside of AWS, while covering concepts such as infrastrucutre, design, routing, and security.
![img](./img/lab-diagram.jpg)

## Solution
1. Create VPC
![img](./img/create-vpc.jpg)
2. Create subnets
![img](./img/subnets.jpg)
3. Create an internet gateway and attache to the VPC created before
![img](./img/igw.jpg)
4. Create a NAT Gateway and associate with the corresponding subnet
![img](./img/nat-gw.jpg)
5. Create two route tables
* Point the public route table to the internet gateway
![img](./img/public-rt.jpg)
* Point the private route table to the NAT gateway
![img](./img/private-rt.jpg)
6. Associate the public and private subnets to the corresponding subnets
7. Create NACL and associate with subnets. You can add inbound and outbound rules to NACL to secure the subnets.
![img](./img/nacl.jpg)

