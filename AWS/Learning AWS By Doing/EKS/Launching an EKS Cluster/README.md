# Launching an EKS Cluster
## Introduction

![img](./img/lab-diagram.jpg)

## Solution
## Create an IAM User with Admin Permissions
1. Navigate to IAM > Users.
2. Click Add user.
3. Set the following values:
    * User name: k8-admin
    * Access type: Programmatic access
4. Click Next: Permissions.
5. Select Attach existing policies directly.
6. Select AdministratorAccess.
7. Click Next: Tags > Next: Review.
8. Click Create user.
9. Copy the access key ID and secret access key, and paste them into a text file, as we'll need them in the next step.
```bash
Access key ID: AKIAXG6GDR36JNGZWNEO
Secret access key: 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
```

## Launch an EC2 Instance and Configure the Command Line Tools
1. Navigate to EC2 > Instances.
2. Click Launch Instance.
3. On the AMI page, select the Amazon Linux 2 AMI.
4. Leave t2.micro selected, and click Next: Configure Instance Details.
5. On the Configure Instance Details page:
    * Network: Leave default
    * Subnet: Leave default
    * Auto-assign Public IP: Enable
6. Click Next: Add Storage > Next: Add Tags > Next: Configure Security Group.
7. Click Review and Launch, and then Launch.
8. In the key pair dialog, select Create a new key pair.
9. Give it a Key pair name of "mynvkp".
10. Click Download Key Pair, and then Launch Instances.
11. Click View Instances, and give it a few minutes to enter the running state.
12. Once the instance is fully created, check the checkbox next to it and click Connect at the top of the window.
13. In the Connect to your instance dialog, select EC2 Instance Connect (browser-based SSH connection).
14. Click Connect.
15. In the command line window, check the AWS CLI version:
```bash
aws --version
# It should be an older version.
```
16. Download v2:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```
17. Unzip the file:
```bash
unzip awscliv2.zip
```
18.See where the current AWS CLI is installed:
```bash
which aws
# It should be /usr/bin/aws.
```
19. Update it:
```bash
sudo ./aws/install --bin-dir /usr/bin --install-dir /usr/bin/aws-cli --update
```
20. Check the version of AWS CLI:
```bash
aws --version
# It should now be updated.
```
21. Configure the CLI:
```bash
aws configure
# For AWS Access Key ID, paste in the access key ID you copied earlier.
# For AWS Secret Access Key, paste in the secret access key you copied earlier.
# For Default region name, enter us-east-1.
# For Default output format, enter json.
```
22. Download kubectl:
```bash
curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.16.8/2020-04-16/bin/linux/amd64/kubectl
```
23. Apply execute permissions to the binary:
```bash
chmod +x ./kubectl
```
24.Copy the binary to a directory in your path:
```bash
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin
```
25.Ensure kubectl is installed:
```bash
kubectl version --short --client
```
26. Download eksctl:
```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
```
27. Move the extracted binary to /usr/bin:
```bash
sudo mv /tmp/eksctl /usr/bin
```
28. Get the version of eksctl:
```bash
eksctl version
```
29.See the options with eksctl:
```bash
eksctl help
```

## Provision an EKS Cluster
1. Provision an EKS cluster with three worker nodes in us-east-1:
```bash
eksctl create cluster --name dev --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed
```
If your EKS resources can't be deployed due to AWS capacity issues, delete your `eksctl-dev-cluster` CloudFormation stack and retry the command using the `--zones` parameter and suggested availability zones from the `CREATE_FAILED` message:
```bash
AWS::EKS::Cluster/ControlPlane: CREATE_FAILED – "Resource handler returned message: \"Cannot create cluster 'dev' because us-east-1e, the targeted availability zone, does not currently have sufficient capacity to support the cluster. Retry and choose from these availability zones: us-east-1a, us-east-1b, us-east-1c, us-east-1d, us-east-1f (Service: Eks, Status Code: 400, Request ID: 21e7e4aa-17a5-4c79-a911-bf86c4e93373)\" (RequestToken: 18b731b0-92a1-a779-9a69-f61e90b97ee1, HandlerErrorCode: InvalidRequest)"
```
In this example, the `--zones` parameter was added using the `us-east-1a,us-east-1b,us-east-1c,us-east-1d,us-east-1f` AZs from the message above:
```bash
eksctl create cluster --name dev --region us-east-1 --zones us-east-1a,us-east-1b,us-east-1c,us-east-1d,us-east-1f --nodegroup-name standard-workers --node-type t3.medium --nodes 3 --nodes-min 1 --nodes-max 4 --managed
```
It will take 10–15 minutes since it's provisioning the control plane and worker nodes, attaching the worker nodes to the control plane, and creating the VPC, security group, and Auto Scaling group.

2. In the AWS Management Console, navigate to CloudFormation and take a look at what’s going on there.
3. Select the `eksctl-dev-cluster `stack (this is our control plane).
4. Click Events, so you can see all the resources that are being created.
5. We should then see another new stack being created — this one is our node group.
6. Once both stacks are complete, navigate to Elastic Kubernetes Service > Clusters.
7. Click the listed cluster.
8. If you see a `Your current user or role does not have access to Kubernetes objects on this EKS cluster message` just ignore it, as it won't impact the next steps of the activity.
9. Click the Compute tab (under Configuration), and then click the listed node group. There, we'll see the Kubernetes version, instance type, status, etc.
10. Click dev in the breadcrumb navigation link at the top of the screen.
11. Click the Networking tab (under Configuration), where we'll see the VPC, subnets, etc.
12. Click the Logging tab (under Configuration), where we'll see the control plane logging info.
    * The control plane is abstracted — we can only interact with it using the command line utilities or the console. It’s not an EC2 instance we can log into and start running Linux commands on.
13. Navigate to EC2 > Instances, where you should see the instances have been launched.
14. Close out of the existing CLI window, if you still have it open.
15. Select the original t2.micro instance, and click Connect at the top of the window.
16. In the Connect to your instance dialog, select EC2 Instance Connect (browser-based SSH connection).
17. Click Connect.
18. In the CLI, check the cluster:
```bash
eksctl get cluster
```
19. Enable it to connect to our cluster:
```bash
aws eks update-kubeconfig --name dev --region us-east-1
```