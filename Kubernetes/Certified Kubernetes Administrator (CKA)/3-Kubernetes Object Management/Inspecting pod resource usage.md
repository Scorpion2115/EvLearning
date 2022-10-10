# Inspecting pod resource usage
kubernetes metrics server: an add-on to collect and provide metrics about the resources pods and containers are using.

## Install
```bash
# a modified version to be compatible with the k8s cluster deployed via kubeadm
kubectl apply -f https://raw.githubusercontent.com/linuxacademy/content-cka-resources/master/metrics-server-components.yaml
```

After installing the add-on, we can uss `kubectl top` to view the metrics
```bash
#kubectl top pod --sort-by <JSONPATH> --selector <selector>

kubectl top pod --sort-by cpu

kubectl top pod --sort-by cpu --all-namespaces
```