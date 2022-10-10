# Using Terraform CLI Commands (workspace and state) to Manipulate a Terraform Deployment
## Introduction
* Create two distinct, parallel environments against the same Terraform code using the terraform workspace command. 
* Use the terraform state command to see what resources are being tracked in the state files of the different workspaces.
## Solution
### Create a New Workspace
1. Check that no workspace other than the default one currently exists:
```bash
terraform workspace list
```
The output should only show the default workspace. This workspace cannot be deleted.

2. Create a new workspace named test:
```bash
terraform workspace new test
```
### Deploy Infrastructure in the Test Workspace and Confirm Deployment via AWS
1. In the test workspace, initialize the working directory and download the required providers:
```bash
terraform init
```
2. Create `main.tf` and `network.tf`
3. Deploy the code in the test workspace:
```bash
terraform apply --auto-approve
```
4. Once the code has executed successfully, confirm that Terraform is tracking resources in this workspace:
```bash
terraform state list
```
There should be a number of resources being tracked, including the resources spun up by the code just deployed.
5. Switch over to the default workspace:
```bash
terraform workspace select default
```
6. Confirm that Terraform is currently not tracking any resources in this workspace, as nothing has been deployed:
```bash
terraform state list

data.aws_availability_zones.azs
data.aws_ssm_parameter.linuxAmi
aws_instance.ec2-vm
aws_security_group.sg
aws_subnet.subnet
aws_vpc.vpc_master
```
The return output should say that No state file was found! for this workspace.
7. Verify that the deployment in the test workspace was successful by viewing the resources that were created in the AWS Management Console: