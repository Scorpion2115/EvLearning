# Backup and Restoring etcd Cluster Data
## Things to do
```bash
ETCDCTL_API=3 etcdctl get cluster.name \
  --endpoints=https://10.0.1.101:2379 \
  --cacert=/home/cloud_user/etcd-certs/etcd-ca.pem \
  --cert=/home/cloud_user/etcd-certs/etcd-server.crt \
  --key=/home/cloud_user/etcd-certs/etcd-server.key
```


## Backup
1. Snapshot using etcdctl options
```bash

ETCDCTL_API=3 etcdctl 
    --endpoints=https://<etcd ip address>:2379 \
    --cacert=<trusted-ca-file> \
    --cert=<cert-file> \
    --key=<key-file> \
    snapshot save <backup-file-location>
```

2. To verify the snapshot
```bash
ETCDCTL_API=3 etcdctl --write-out=table snapshot status <backup-file-location>

+----------+----------+------------+------------+
|   HASH   | REVISION | TOTAL KEYS | TOTAL SIZE |
+----------+----------+------------+------------+
| 68ae77f5 |        2 |          5 |      20 kB |
+----------+----------+------------+------------+
```

3. Reset etcd by removing all existing etcd data:
```bash
sudo systemctl stop etcd
sudo rm -rf /var/lib/etcd
```

## Restore
```bash
ETCDCTL_API=3 etcdctl --endpoints 10.2.0.9:2379 snapshot restore snapshotdb
```

