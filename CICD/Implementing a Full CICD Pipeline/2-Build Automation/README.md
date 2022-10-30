# Build Automation
Build automation is the automation of tasks needed in order to process and prepare source code for deployment to production.
- Compiling
- Dependency Management
- Executing Automated Tests
- Packaging the app for Deployment

## Gradle Basic
- Define tasks
- Define task Dependency
- Add plugins to take advantage of pre-built Gradle tasks created by the Gradle community?

1. Create a project and initialize it
```bash
mkdir ev-project
cd ev-project
gradle init
```
2. Edit build.gradle
```java
/* add plugin*/
plugins {
id 'com.moowork.node' version '1.2.0'
}

task sayHello {
doLast {
println 'Hello, World!'
}
}

task anotherTask {
doLast {
println 'This is another task'
}
}

/* define task dependency */
sayHello.dependsOn anotherTask
```
3. Run gradle wrapper
```bash
# run SayHello Test
./gradlew sayHello

> Task :anotherTask
This is another task

> Task :sayHello
Hello, World!

# run anotherTask
./gradlew anotherTask

> Task :anotherTask
This is another task

BUILD SUCCESSFUL in 1s
1 actionable task: 1 executed
cloud_user@4dba7187062c:~/jenkins/ev-project$ 
```

## Automated Testing
Automated tests are usually codes that are written to test other codes.
- Unit Test: test single function
- Integration Test: test large portion of an application that are integrated with each other
- Smoke Test/Sanity Test: High level integration tests to verify basic, large-scale thinks.