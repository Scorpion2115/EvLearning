# Installing Terraform and Working With Terraform Providers
## Download And Manually Install the Terraform Binary
1. Download the appropriate Terraform binary package for the provided lab server VM (Linux 64-bit) using the wget command:
```bash
wget -c https://releases.hashicorp.com/terraform/0.13.4/terraform_0.13.4_linux_amd64.zip
```
2. Unzip the downloaded file:
```bash
unzip terraform_0.13.4_linux_amd64.zip
```
3. Place the Terraform binary in the PATH of the VM operating system so the binary is accessible system-wide to all users:
```bash
sudo mv terraform /usr/sbin/
```
4. Check the Terraform version information:
```bash
terraform version
```

## Clone Over Code for Terraform Providers
1. Create a providers directory:
```bash
mkdir providers

cd providers/
```
2. Create the file `main.tf`:Paste in the following code from the provided GitHub repo:

## Deploy the Code with Terraform Apply
1. Enable verbose output logging for Terraform commands using TF_LOG=TRACE:
```bash
export TF_LOG=TRACE
```
2. Initialize the working directory where the code is located:
```bash
terraform init
```
3. Review the actions performed when you deploy the Terraform code:
```bash
terraform plan
```
Note: Two resources will be created, consistent with the providers that were configured in the provided code snippet.

4. Deploy the code:
```bash
terraform apply
```
5. Verify that two resources were created with their corresponding Amazon Resource Name (ARN) IDs in the region in which they were spun up.

6. Tear down the infrastructure you just created before moving on:
```bash
terraform destroy --auto-approve
```