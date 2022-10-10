# Install Terraform
## Install in Ubuntu
1. Ensure that your system is up to date, and you have the gnupg, software-properties-common, and curl packages installed. You will use these packages to verify HashiCorp's GPG signature, and install HashiCorp's Debian package repository.
```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
```
2. Install the HashiCorp GPG key.
```bash
wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
```
3.Verify the key's fingerprint.
```bash
gpg --no-default-keyring \
    --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    --fingerprint
```
4. Add the official HashiCorp repository to your system. The lsb_release -cs command finds the distribution release codename for your current system, such as buster, groovy, or sid.
```bash
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list
```

5. Download the package information from HashiCorp.
```bash
sudo apt update
```
6. Install Terraform from the new repository.
```bash
sudo apt-get install terraform
```
## Verify the installation
1. Verify that the installation worked by opening a new terminal session and listing Terraform's available subcommands.
```bash
terraform -help
```

## Quick Start
1. Paste the following Terraform configuration into a file and name it `main.tf`
```bash
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}
```
2. Initialize the project, which downloads a plugin that allows Terraform to interact with Docker.
```bash
sudo terraform init
```
3.Provision the NGINX server container with apply. When Terraform asks you to confirm type yes and press ENTER.
```bash
sudo terraform apply
```




