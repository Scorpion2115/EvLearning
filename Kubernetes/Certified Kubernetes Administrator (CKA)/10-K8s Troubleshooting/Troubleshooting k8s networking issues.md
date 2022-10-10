# Troubleshooting k8s networking issues
## kube-proxy and DNS
```bash
kubectl get po -n kube-system
```
## netshoot
You can run a container in the cluster that you can run commands to test and gather information about the network functionality

The `nicolaka/netshoot` image is a great tool for this. Create a container running this image, and then use `kubectl exec` to explore away
```bash
kubectl exec --stdin --tty netshoot -- /bin/sh
```