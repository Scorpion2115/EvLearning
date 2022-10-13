# CodeCommit
## Key Factor
CodeCommit is a managed service that host private Git repositories.
Benefit:
* HA, FT and scalable
* No size limit
* Integrates with other AWS services (CodeBuild, CodeDeploy, CodePipeline, Lambda, SNS)

## Sandbox
1. Create IAM users in AWS
- Create two IAM Users with full access to CodeCommit
- Generate HTTPS Git credentials for AWS CodeCommit and keep the credentials
```bash
# user1
ev-at-452750642022
+aWzcJOideiqhWLA1Rb6RCe0vNSNe7lvlDrnyVUrnrs=

# user2
jas-at-452750642022
Bjimphn1ArLbZauOKsYgRL3nfv0T/w21xvijEl45FPo=
```
![img](./img/iam-user.jpg)

2. Configure aws cli 
```bash
aws configure
AWS Access Key ID []: AKIAVLVIJ6CL7JH7O7IG
AWS Secret Access Key []: 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
Default region name []: us-east-1
Default output format [None]: 
```

## CodeCommit Repository Action in CLI

### Repository Actions
Commands:
- Create:`aws codecommit create-repository --repository-name <my-repo>`
- List: `aws codecommit list-repositories`
- View: `aws codecommit get-repository --repository-name <my-repo>`
- Delete: `aws codecommit delete-repository --repository-name <my-repo>`

### Clone, Commit, Push and Pull
Commands:
```bash
git clone
git add -A
git commit -m "xx"
git push
```

### Merge and Branch
Why Branch:
- Add new features
- Fix Bugs
- Without disrupting the master branche

Commands:
1. Create a test branch and push code as user jas
```bash
git branch # create a new branch

git checkout # create and switch to a new branch

git push --set-upstream origin test
```

2. Switch back to the master branch and trigger a merge
```bash
git checkout master # switch back to the main branch

git merge test # merge

git push

git branch -d test # delete the test branch
```

## Data Security
At rest: CodeCommit encrypt the data which are stored in the repository
In transit: SSH or HTTPS
Extra: AWS will create an encrypting key for each repository we create in CodeCommit
![img](./img/security.jpg)

### Data Security Scenario
Scenario: You want your development team to have full access to CodeCommit, but they should not be able to create or delete repositories.

Solution: 
- Attach the `AWSCodeCommit PowerUser` policy to the account of each developer. 
- Create an `IAM group` to manage the developers in one place and attach that policy to the group. 
![img](./img/security-scenario.jpg)