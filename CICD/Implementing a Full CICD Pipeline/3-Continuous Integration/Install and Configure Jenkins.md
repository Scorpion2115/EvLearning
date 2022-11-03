# Install and Configure Jenkins
## Install java
```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
```
## Install Jenkins
1. Start by importing the GPG key. The GPG key verifies package integrity but there is no output. Run:
```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
```
2. Add the Jenkins software repository to the source list and provide the authentication key:
```bash
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```
3. Install Jenkins
```bash
sudo apt-get update
sudo apt install jenkins -y
```
4. Modify Firewall to Allow Jenkins
```bash
sudo ufw allow 8080
sudo ufw status

#Status: inactive
```
5. Access the UI via `<host-ip>:8080`

## Configure Jenkins
0. Generate a Personal access tokens from Github via `Settings -> Developer settings` with `admin:repo_hook` privilege.
1. Add the access token to Jenkins via In Manage-Jenkins -> Configure System
![img](./img/token.jpg)
1. Create a new FreeStyle project in Jenkins, and paste the url of source code project to `Source Code Management`
2. Build Triggers - GitHub hook trigger for GITScm polling
3. Build Steps - Invoke Gradle script
- Check Use `Gradle Wrapper`
- Input the tasks name, as per `build.gradle` in the source code
4. Post-build Actions - Archive the artifacts
![img](./img/build-steps.jpg)

## Issue Fix
- Issue: [Gradle: Could not determine java version from '11.0.6'](https://stackoverflow.com/questions/54358107/gradle-could-not-determine-java-version-from-11-0-2). You need update gradle wrap version and push it to repo
![img](./img/issue-fix-graddle-wrapper.jpg)

- Issue: [Could not find method layout() on upgrading to gradle 7.2](https://discuss.gradle.org/t/could-not-find-method-layout-on-upgrading-to-gradle-7-2/41194). If you need to run Node tasks in your Gradle build, migrate to a plugin that is still maintained, like the com.github.node-gradle.node 12 Gradle Node plugin.

## Reference
- [How to Install Jenkins on Ubuntu 22.04](https://phoenixnap.com/kb/install-jenkins-ubuntu)
