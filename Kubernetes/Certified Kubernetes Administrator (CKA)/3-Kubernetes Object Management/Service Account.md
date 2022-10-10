# Service Account
A service account is an account used by container processes within pods to authenticate with the k8s API

If your pods need to communicate with the k8s API, you can use service accounts to control the access

[Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)

You can manage access control for service accounts, using RBAC objects.