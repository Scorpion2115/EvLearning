# Cheat Sheet

## Object Management:
1. The ensure a worker node is ready to run normal workloads, you need check if the worker node is tainted
```bash
kubectl describe node  acgk8s-worker1|grep Taints
```

2. 
```bash
kubectl top pod -n web --sort-by cpu --selector app=auth
```

## Backup etcd
1. Skelton - backup
```bash
ETCDCTL_API=3 etcdctl --endpoints <ip address>:2379 \
--cert=</path/crt> \
--key=</path/key> \
--cacert=</path/pem \
snapshot save </path/name-of-backup>
```
2. Skelton - restore
```bash
# stop etcd
sudo systemctl stop etcd

# remove etcd
sudo rm -rf /var/lib/etcd

# restore to the nominated directory
sudo ETCDCTL_API=3 etcdctl --endpoints 10.0.1.102:2379 \
snapshot restore etcd_backup.db \
--data-dir /var/lib/etcd
```

## Scheduling
```bash
```


## Bash
Quick notes
```bash
# echo "your notes" > path/file-name
echo 2 > /k8s/0001/count.txt

kubectl logs data-handler  -n backend|grep ERROR > /k8s/0002/errors.txt
```

## Deployment 
1. Scale up the deployment:
```bash
# ubectl scale deployment <deployment name> -n <namespace> --replicas=<number of replicas>
kubectl scale deployment web-frontend -n web --replicas=5
```

## RBAC
1. Resources for a role
```bash
resources: ["nodes", "pods", "configmaps", "deployments"]
```

2. Subjects om RoleBinding
* ServiceAccount
* Group
* User

## Storage
The sequence of deploy a pod using local disk as persistent volume
1. Create a `StorageClass`:
```yml
...
metadata:
  name: <the-name-of-sc>
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
...
``` 
2. Create a `PV`
```yml
...
metadata:
  name: <my-pv>
spec:
  storageClassName: <the-name-of-sc>
...
```
3. Create a `PVC`
```yml
...
metadata:
  name: <my-pvc>
  namespace: <my-ns>
spec:
  storageClassName: <the-name-of-sc>
...
```

## kubectl
```bash
kubectl top pod -n web --sort-by cpu --selector app=auth  # Show metrics for a given pod with specific label and sort it by 'cpu' or 'memory'

kubectl get nodes --show-labels                                  # Show labels
kubectl get pods -l key1=value1,key2=value2                      # Search pod based on its labels

kubectl label nodes <node-name> key=value                      # Add a Label
```

## Scaling resources
```bash
kubectl scale --replicas=3 rs/foo                                 # Scale a replicaset named 'foo' to 3
kubectl scale --replicas=3 -f foo.yaml                            # Scale a resource specified in "foo.yaml" to 3
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql  # If the deployment named mysql's current size is 2, scale mysql to 3
kubectl scale --replicas=5 rc/foo rc/bar rc/baz                   # Scale multiple replication controllers
```


## Interacting with running Pods
```bash
kubectl logs my-pod                                 # dump pod logs (stdout)
kubectl logs -l name=myLabel                        # dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod --previous                      # dump pod logs (stdout) for a previous instantiation of a container
kubectl logs my-pod -c my-container                 # dump pod container logs (stdout, multi-container case)
kubectl logs -l name=myLabel -c my-container        # dump pod logs, with label name=myLabel (stdout)
kubectl logs my-pod -c my-container --previous      # dump pod container logs (stdout, multi-container case) for a previous instantiation of a container
kubectl logs -f my-pod                              # stream pod logs (stdout)
kubectl logs -f my-pod -c my-container              # stream pod container logs (stdout, multi-container case)
kubectl logs -f -l name=myLabel --all-containers    # stream all pods logs with label name=myLabel (stdout)
kubectl run -i --tty busybox --image=busybox:1.28 -- sh  # Run pod as interactive shell
kubectl run nginx --image=nginx -n mynamespace      # Start a single instance of nginx pod in the namespace of mynamespace
kubectl run nginx --image=nginx                     # Run pod nginx and write its spec into a file called pod.yaml
--dry-run=client -o yaml > pod.yaml

kubectl attach my-pod -i                            # Attach to Running Container
kubectl port-forward my-pod 5000:6000               # Listen on port 5000 on the local machine and forward to port 6000 on my-pod
kubectl exec my-pod -- ls /                         # Run command in existing pod (1 container case)
kubectl exec --stdin --tty my-pod -- /bin/sh        # Interactive shell access to a running pod (1 container case)
kubectl exec my-pod -c my-container -- ls /         # Run command in existing pod (multi-container case)
kubectl top pod POD_NAME --containers               # Show metrics for a given pod and its containers
kubectl top pod POD_NAME --sort-by=cpu              # Show metrics for a given pod and sort it by 'cpu' or 'memory'
```