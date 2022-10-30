# Install and Configure Jenkins
## Install Jenkins
```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```
Access the UI via `<host-ip>:8080`

## Configure Jenkins
1. Create a new FreeStyle project in Jenkins, and paste the url of source code project to `Source Code Management`
2. Build Steps - Invoke Gradle script
- Check Use `Gradle Wrapper`
- Input the tasks name, as per `build.gradle` in the source code
3. Post-build Actions - Archive the artifacts
![img](./img/build-steps.jpg)



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