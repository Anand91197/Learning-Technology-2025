# Scale the Deployment Up to 5
kubectl scale deployment demo-deployment --replicas=5

➡️ You’ll now have 5 pods running.


# Scale Down to 2
kubectl scale deployment demo-deployment --replicas=2

➡️ Now only 2 pods remain; the rest are terminated.

# Clean Up
kubectl delete -f my-deploy.yaml

# Update Deployment:-
kubectl describe deployments demo-deployment

kubectl set image deployment/demo-deployment nginx=nginx:1.28.0

# To see roll out status:
kubectl rollout status deployment/demo-deployment

# To see roll out history:

kubectl rollout history deployment/demo-deployment

# To see each revision history:

kubectl rollout history deployment/demo-deployment --revision=2

# Rolling Back to a Previous Revision:

kubectl rollout undo deployment/demo-deployment

Or

(Specific revision)
kubectl rollout undo deployment/demo-deployment--to-revision=2

kubectl describe deployment demo-deployment


======
## Expose Service of the Deployment

# Expose Using NodePort
kubectl expose deployment webapp-deployment --type=NodePort --name=webapp-service

http://<NODE_IP>:<NodePort>
curl http://<your-node-ip>:31234

# Internal Access via ClusterIP

kubectl expose deployment webapp-deployment --type=ClusterIP --name=webapp-internal

Run a temporary pod:
kubectl run test-client --rm -it --image=busybox -- /bin/sh


Inside the shell:
wget -qO - http://webapp-internal

========

# Apply:-
kubectl apply -f nginx-deployment.yml 

kubectl get pods -o wide

 kubectl get svc -o wide


 kubectl get nodes -o wide

 # Verifiy:

 curl http://10.202.6.211:31676
===

# To check Server/Master
kubectl config view --minify | grep server

# Binding Object to another Node

kubectl config view --minify | grep server
curl --header "Content-Type: application/json" --request POST --data @binding.json http://10.202.19.162:6443/api/v1/namespaces/default/pods/nginx/binding

=
# Directly binding a Pod to a specific node using the /binding endpoint of the Kubernetes API is not the standard or recommended way to control where a Pod runs after it's already scheduled or to reschedule it. Kubernetes's scheduler is responsible for assigning Pods to nodes. If a Pod is already running, it's typically tied to that node.


# Continue monitoring the pod status until it reaches the Running state:

kubectl get pods --watch

# Remember that you cannot relocate a running pod from one node to another. Instead, delete the existing pod and recreate it on the desired node using the kubectl replace --force command; update the node name in the YAML and then run below
kubectl replace --force -f nginx.yaml

==
# Port Forwarding
# This forwards traffic from your local machine's port 8080 to port 80 inside the my-nginx-deployment-abcde-fghij Pod. You can then access it via http://localhost:8080 on your local machine.
kubectl port-forward my-nginx-deployment-abcde-fghij 8080:80

====
# Labels are key-value pairs attached to Kubernetes objects like Pods, Deployments, Services, etc. They help organize, filter, and group resources.

# Selectors are used by Kubernetes components (like Services, Deployments) to select matching objects based on their labels. It’s how Kubernetes knows which Pods belong to which Service or Deployment.
===
# Taints-Tolerations

# Apply:- 
kubectl taint nodes kube-node-1 app=blue:NoSchedule

# Remove
kubectl taint nodes kube-node-1 app=blue:NoSchedule-
===
# Remove Label

kubectl label node <node-name> <label-key>-
kubectl label node node-1 disktype-

==
# Static Pod Creation

kubectl run static-busybox --image=busybox --restart=Never --dry-run=client -o yaml > static-busybox.yaml

# Copy this static-busybox.yaml file to path /etc/kubernetes/manifests/ and kubelet will create a static pod.
# If want to delete it then need to remove the YAML file from the path.
===

# Secrets You must base64 encode values manually (or via echo):
echo -n 'admin' | base64        # YWRtaW4=
echo -n 'password' | base64     # cGFzc3dvcmQ=
==
# Kubeconfig
export KUBECONFIG=/path/to/my-kubeconfig.yml
===
# To Access API Server
curl http://localhost:6443 -k --key admin.key --cert admin.crt --cacert ca.crt


# To get Certificate from the Kube-Config:

kubectl config view --raw -o jsonpath='{.clusters[0].cluster.certificate-authority-data}' | base64 --decode > ca.crt

kubectl config view --raw -o jsonpath='{.users[0].user.client-certificate-data}' | base64 --decode > admin.crt

kubectl config view --raw -o jsonpath='{.users[0].user.client-key-data}' | base64 --decode > admin.key

==
# Check what can do
kubectl auth can-i create deployments
kubectl auth can-i delete nodes

For specific User:
kubectl auth can-i create deployments --as dev-user
==

# Network Policy

The podSelector targets the database pod through its label.
The policyTypes field specifies that only ingress traffic is affected.
The ingress rule allows traffic specifically from pods with the label name: api-pod on TCP port 3306.

If no ingress rules are specified, Kubernetes treats the policy as a complete block for incoming traffic.