# Managing Rolling Updates with Deployments
## What is a rolling update
Rolling updates allow you to make changes to a deployment's pods at a controlled rate, gradually replacing old pods with new ones.

This allows you to update your pods without incurring downtime

To see what is happening with the rolling updates
```bash
kubectl rollout status deployment.v1.apps/my-deployment
```


## What is a rollback
If an update to a deployment have any issue, you can rollback the deployment to the previous working state

Perform another rollout, this time using the kubectl set image method. Intentionally use a bad image version.
```bash
kubectl set image deployment/my-deployment nginx=nginx:broken --record
```

Roll back to an earlier working version with one of the following methods.
```bash
# rollback to the previous version
kubectl rollout undo deployment.v1.apps/my-deployment

# rollback to a specific version
kubectl rollout undo deployment.v1.apps/my-deployment --to-revision=<a specific version>
```