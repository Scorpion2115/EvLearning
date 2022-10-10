# Troubleshooting your applications
## Investigate the pod
```bash
kubectl describe pods <pod-name> -n <namespace>
```

## Running Commands inside the pod
```bash
kubectl exec <pod-name> -n <namespace> -c <container-name> -- command
```
