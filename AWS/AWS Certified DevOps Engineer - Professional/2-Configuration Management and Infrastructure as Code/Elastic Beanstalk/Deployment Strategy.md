# Deployment Strategy
## Environment Types
![img](../img/eb-deploy-strategy.jpg)
Single Instance:
* Load balancer
* Auto scaling group: always keep one single instance,  Elastic IP address

High Availability:
* Load balancer
* Auto scaling group: provide a group of instances

## Deployment Methods
![img](../img/eb-deployment-method.jpg)
