# Deploy Presto via Kubernetes
1. Clone the original repo
```bash
git clone https://github.com/Ahana-Inc/presto-getting-started 
```

2. Build the image
```bash
sudo docker build -t evan21/prestodb .

# verify the image
sudo docker images
```
3. Push the image to Dockerhub
```bash
docker login --username=evan21
sudo docker push evan21/prestodb
```
4. Deploy MySQL for demo purpose
```bash
kubectl create ns presto

kubectl apply -f mysql-pv.yaml -n presto
kubectl apply -f mysql-deployment.yaml -n presto

# Verify connectivity / working database 
kubectl run -it --rm --image=mysql:5.7 --restart=Never mysql-client -n presto -- mysql -h mysql -udbuser -pdbuser

```

5. Deploy Presto
```bash
kubectl apply -f presto.yaml -n presto
```
6. Verify
```bash
kubectl exec -it <pod name> -n presto -- bash

# open presto cli
presto

# display catalogs
presto> show catalogs;
  Catalog  
-----------
 blackhole 
 hive      
 jmx       
 mysql     
 system    
 tpcds     
 tpch      

# confirm connectivity to mysql instance

show schemas from mysql;
```