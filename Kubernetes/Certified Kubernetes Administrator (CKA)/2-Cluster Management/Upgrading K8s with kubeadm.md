# Upgrading K8s with kubeadm

## Control Node Upgrade Step
1. Upgrade `kubeadm` on the control plane node
2. Drain the control plane node
3. Plan the upgrade
```bash
kubeadm upgrade plan
```
4. Apply the upgrade
```bash
kubeadm upgrade apply
```
5. Upgrade kubelet and kubectl on the control plane
6. Uncordon the control node

## Worker Node Upgrade Step
1. Drain the worker nodes
2. Upgrade kubeadm 
3. Upgrade the kubelete configuration
```bash
kubeadm upgrade node
```
5. Upgrade kubelet and kubectl on the control plane
6. Uncordon the worker node

## Lab
[Performing a Kubernetes Upgrade with kubeadm](./Lab/Perform%20a%20Kubernetes%20Upgrad%20with%20kubeadm/)