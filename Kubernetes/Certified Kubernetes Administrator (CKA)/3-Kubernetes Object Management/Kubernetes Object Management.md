# Kubernetes Object Management

## Working with kubectl
[Exploring a kubernetes cluster using kubectl](./Lab/Exploring%20a%20kubernetes%20cluster%20using%20kubectl)

## kubectl tips
Declarative command: Define objects using ymal or json
Imperative command: Define object using `kubectl` and flags
1. Use `dry-run` to run an imperative command without creating an object. Combine it with `-o yaml` to quickly obtain a sample ymal file you can manipulate.
```bash
kubectl create deployment my-deployment --image=ngnix --dry-run -o yaml
```
2. Use `record` flag to record the command that was used to make a change
```bash
kubectl scale deployment my-deployment replicas=5 --record
```