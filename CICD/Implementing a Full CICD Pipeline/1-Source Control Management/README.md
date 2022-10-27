# README
## Introduction to SCM
SCM (Source Control Management) is an important component of CI/CD Pipeline
All pieces of automation need to interact with SCM:
* CI will get the code from SCM
* SCM will notify the CI server when code needs to be built

Git SCM
* Clone
* Add
* Commit
* Push
* Branch
* Merge
* Pull Requests: To allow review prior to a merge. Once you commit a source change to a branch, you can submit a request for the branch to be merged, you can review the merge that is performed.

## Git
1. Configure Git
```bash
git config --global user.name"<you-know-who>"
git config --global user.email"<you-know-who>"
```

2. Setting up private key access
```bash
# generate the key pair
ssh-keygen

# copy the publick to Github -> Settings -> SSH and GPG Keys
cat /home/cloud_user/.ssh/id_rsa.pub
# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNemAeCVu0hWBW0fuNJVV+A1XKZsVtdUYaBGOgcpXXdHoLz+z3Rrlk+9dhWuOmUU2VQTWVHxtSuUqd5zRSduYuJ0GVeUpXaLxXz3vclUiTqlnDdFH24RyttjsmVgps5KBGQ8dz1cTAQqJM5WK/uCExDZj/ZzT1+svG0ylysJPsC8NMs80Hyf4IwxJUoy0m7hSgVRNiFJpyeqDea7eyF1EobZ+AkV/pzmAJO2oU9NuBSpFSlAHmkxSLRMS0RdHqeKqNOMjVVT13eS0ZNE/EGdzb1kfWucrJvFA98Rz9Fuc0fy+cUDsPdhD8UH+T3XIC2lWIngsQ2nyM2bjetZ9LzWW+tiz5Pt94cHYMSo274tmSKiJRF3gwqg9NyJGOPghnEtnmed3fR/APofpQZF3GPBTjpghFv7WyIjvjDmaZfGTnxWGR0sbvE0syZbARb/YnX+vffY51Va+GAHPMhna89BVRJju4WNE+sOx9Sdz2pyVMTpQIebUzP17LjoSF1NnI1ZE= cloud_user@4dba7187062c.mylabserver.com
```
## Pull Request
A developer makes a pull request to make their changes merge into another brance. It give other team members a chance to review the changes first, before the merge is actually performed.