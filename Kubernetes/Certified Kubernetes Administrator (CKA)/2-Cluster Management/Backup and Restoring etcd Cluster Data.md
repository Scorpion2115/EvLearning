# Backup and Restoring etcd Cluster Data
## Why backup etcd
etcd is the backend data sotrage solution for k8s cluster. As such, all the k8s objects, applications and configurations are stored in etcd.
Periodically backing up the etcd cluster data is important to recover Kubernetes clusters under disaster scenarios


## Backup
etcd supports built-in snapshot. A snapshot may either be taken from a live member with the `etcdctl snapshot save` command
```bash
ETCDCTL_API=3 etcdctl --endpoints $ENDPOINT snapshot save <file name>

# Snapshot using etcdctl options
ETCDCTL_API=3 etcdctl 
    --endpoints=https://<etcd ip address>:2379 \
    --cacert=<trusted-ca-file> \
    --cert=<cert-file> \
    --key=<key-file> \
    snapshot save <backup-file-location>


# to verify the snapshot
ETCDCTL_API=3 etcdctl --write-out=table snapshot status <file name>
```

## Restore
```bash
ETCDCTL_API=3 etcdctl --endpoints <etcd ip address>:2379 snapshot restore <file name>

ETCDCTL_API=3 etcdctl snapshot restore <file name>

ETCDCTL_API=3 etcdctl --data-dir <data-dir-location> snapshot restore <file name>
```

## Labs