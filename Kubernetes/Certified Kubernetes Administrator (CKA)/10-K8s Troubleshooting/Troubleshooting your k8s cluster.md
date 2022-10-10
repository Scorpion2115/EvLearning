# Troubleshooting your k8s cluster
## Kube API Server
If the k8s API server is down, you are not able to use kubectl to interact with the cluster

Possible fixes:
Make sure `docker` and `kubelet` services are up and running on your control plane
```bash
sudo systemctl status kubelet
```

## Checking Node Status
`kubectl get nodes`

## Checking System Pods
`kubectl get pods -n kube-system`

