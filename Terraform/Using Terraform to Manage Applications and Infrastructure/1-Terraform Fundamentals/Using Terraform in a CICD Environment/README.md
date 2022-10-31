# Using Terraform in a CI/CD Environment
![img](./img/lab-diagram.jpg)
## Target
* Setup Terraform Cloud
* Setup Github Repository
* Action Workflow
* Create and Merging pull request
* Verifying a provisioning Instance

## Solution
### Setup Terraform Cloud
1. Start from scratch
2. Create organization
3. Create API-Driven workflow
4. Add AWS `Access Key ID` and `Secret Access Key` as environment variables
5. Create an API token
```bash
bCnlGiorbLPyqA.atlasv1.SUkuOlXuoxMjBqgcJ5zWnynffRA7MTtZYJlUF4hTCK0GMKMOojAQOcTy99jwxxl172w
```

### Setup Github Repository
1. Fork the provided repo
2. Create a new secret named `TF_API_TOKEN`
3. Use Terraform API token above
![img](./img/github.jpg)
4. Enable the pre-configure workflow
![img](./img/workflow.jpg)
5. Clone the Terraform Github Action repository in the terraform controller VM

### Action Workflow
1. `.github/workflows/terraform.yml` in a hidden directory 
2. `main.tf`

### Create and Merging pull request
1. Create a new branch in your repo called `update-tfc-backend`
```bash
git checkout -b 'update-tfc-backend'
```
2. Update the `main.tf` file with your terraform cloud organization and workspace
3. Add, commit, and push your changes
4. Review and merge the pull request

### Verifying a provisioning Instance
