# How to Install Gradle on Ubuntu 22.04
1. Install Java on Ubuntu
```bash
sudo apt install openjdk-8-jdk -y

java -version
```
2. Download Gradle package
```bash
wget -c https://services.gradle.org/distributions/gradle-7.5.1-bin.zip -P /tmp
```
3. Unzip the downloaded package of Gradle
```bash
sudo unzip -d /opt/gradle /tmp/gradle-7.5.1-bin.zip
```
4. Set up environment variables
```bash
sudo vi /etc/profile.d/gradle.sh
```
Add these two lines
```sh
export GRADLE_HOME=/opt/gradle/gradle-7.5.1

export PATH=${GRADLE_HOME}/bin:${PATH}
```
5. Change the permissions of file
```bash
sudo chmod +x /etc/profile.d/gradle.sh
```
6. Install the Gradle
```bash
source /etc/profile.d/gradle.sh
```
7. Verify the installation
```bash
gradle --version

Welcome to Gradle 7.5.1!

Here are the highlights of this release:
 - Support for Java 18
 - Support for building with Groovy 4
 - Much more responsive continuous builds
 - Improved diagnostics for dependency resolution

For more details see https://docs.gradle.org/7.5.1/release-notes.html


------------------------------------------------------------
Gradle 7.5.1
------------------------------------------------------------

Build time:   2022-08-05 21:17:56 UTC
Revision:     d1daa0cbf1a0103000b71484e1dbfe096e095918

Kotlin:       1.6.21
Groovy:       3.0.10
Ant:          Apache Ant(TM) version 1.10.11 compiled on July 10 2021
JVM:          11.0.16 (Ubuntu 11.0.16+8-post-Ubuntu-0ubuntu120.04)
OS:           Linux 5.15.0-1022-aws amd64
```
## Reference
- [How to Install Gradle on Ubuntu 22.04](https://linuxhint.com/installing_gradle_ubuntu/)