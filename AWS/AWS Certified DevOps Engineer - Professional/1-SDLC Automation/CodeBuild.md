# CodeBuild
CodeBuild is a fully managed CI service that compiles source code, runs tests, and produce software packages that are ready to deploy

## How does CodeBuild Work
![img](./img/codebuild-work-flow.jpg)
1. Provide with a build project
2. Use the Build project to create build environment
3. Download Source Code to the build environment
4. Send output of the build to S3
5. While a build is running, the build project can send information to CloudWatch or back to CodeBuild
6. Use preferred interface to get update