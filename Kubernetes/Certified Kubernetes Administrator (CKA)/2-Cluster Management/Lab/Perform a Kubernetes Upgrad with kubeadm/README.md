# Performing a Kubernetes Upgrade with kubeadm

## Control Node Upgrade Step
1. Upgrade `kubeadm` on the control plane node
```bash
# check the kubeadm version
sudo kubeadm version

# update repo
sudo apt update

# Determine which version to upgrade to
sudo apt-cache madison kubeadm

# Upgrade
sudo apt-mark unhold kubeadm
sudo apt-get install -y kubeadm=1.23.10-00
sudo apt-mark hold kubeadm
```

2. Plan the upgrade
```bash
sudo kubeadm upgrade plan
```
3. Apply the upgrade
```bash
sudo kubeadm upgrade apply v1.23.10
```
4. Drain the control plane node
```bash
kubectl drain <node-to-drain> --ignore-daemonsets
```
5. Upgrade `kubelet` and `kubectl` on the control plane
```bash
# upgrade
sudo apt-mark unhold kubelet kubectl
sudo apt-get install -y kubelet=1.23.10-00 kubectl=1.23.10-00
sudo apt-mark hold kubelet kubectl

# Restart kubelete
sudo systemctl daemon-reload
sudo systemctl restart kubelet
```
6. Uncordon the control node
```bash
kubectl uncordon k8s-control 
```

## Worker Node Upgrade Step
1. Upgrade `kubeadm` on the control plane node
```bash
# check the kubeadm version
sudo kubeadm version

# update repo
sudo apt update

# Upgrade
sudo apt-mark unhold kubeadm
sudo apt-get install -y kubeadm=1.23.10-00
sudo apt-mark hold kubeadm
```

2. Apply the upgrade
```bash
sudo kubeadm upgrade node
```
3. Drain the control plane node
```bash
kubectl drain <node-to-drain> --ignore-daemonsets
```
4. Upgrade `kubelet` and `kubectl` on the control plane
```bash
# upgrade
sudo apt-mark unhold kubelet kubectl
sudo apt-get install -y kubelet=1.23.10-00 kubectl=1.23.10-00
sudo apt-mark hold kubelet kubectl

# Restart kubelete
sudo systemctl daemon-reload
sudo systemctl restart kubelet
```
6. Uncordon the control node
```bash
kubectl uncordon <node-to-drain>
```

## Verify the status of the cluster
```bash
kubectl get node

NAME          STATUS   ROLES                  AGE   VERSION
k8s-control   Ready    control-plane,master   51m   v1.23.10
k8s-worker1   Ready    <none>                 50m   v1.23.10
k8s-worker2   Ready    <none>                 50m   v1.23.10
```


## Reference
[Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)