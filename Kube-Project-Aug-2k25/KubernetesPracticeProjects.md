Project 1: Deploy a Stateless Web Server 🌐
Goal: Deploy a simple Nginx web server using a Deployment and expose it to the outside world using a NodePort Service. This covers the basics of running and accessing a stateless application.Prerequisites:A running Kubernetes cluster (like Minikube, Kind, or a cloud-based one).kubectl configured to communicate with your cluster.Solution 
Steps:1 Create the Deployment YAML
Save this content as nginx-deployment.yaml:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21.6 # Using a specific version is good practice
        ports:
        - containerPort: 80
2. Apply the DeploymentIn your terminal, run:kubectl apply -f nginx-deployment.yaml
3. Verify the Deployment and PodsCheck that the Deployment created the Pods and that they are running.# Check the deployment status
kubectl get deployment nginx-deployment

# Check the running pods
kubectl get pods -l app=nginx -o wide
You should see two nginx pods with a STATUS of Running.4. Create the NodePort Service YAMLThis file defines how to expose your Nginx pods to traffic from outside the cluster.Save this content as nginx-service.yaml:apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx # This must match the labels on your pods
  ports:
    - protocol: TCP
      port: 80       # Port inside the cluster
      targetPort: 80 # Port on the container
      # nodePort: 30007 # Optional: You can specify a port or let Kubernetes choose one
5. Apply the ServiceIn your terminal, run:kubectl apply -f nginx-service.yaml
6. Access the Nginx ServerFind the IP address of one of your worker nodes and the NodePort assigned by the service.# Get the NodePort
kubectl get service nginx-service

# Get the IP address of your nodes
kubectl get nodes -o wide
The output of get service will show the port mapping (e.g., 80:3XXXX/TCP). Use the IP of any worker node and the assigned NodePort (the one in the 30000 range) to access your Nginx server in a web browser or with curl.curl http://<WORKER_NODE_IP>:<NODE_PORT>
You should see the "Welcome to nginx!" page.

=======

Project 2: Manage Application Configuration with ConfigMaps ⚙️
Goal: Deploy a simple application that reads its configuration from a ConfigMap. This teaches you how to decouple configuration from your application code.
Steps:1. Create the ConfigMap YAML
This file will hold configuration data (in this case, a custom message).Save this content as app-configmap.yaml:
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-app-config
data:
  MESSAGE: "Hello from a ConfigMap!"
  APP_VERSION: "v1.1"
2. Apply the ConfigMapkubectl apply -f app-configmap.yaml
3. Create the Pod YAML
This Pod will mount the ConfigMap values as environment variables.Save this content as config-pod.yaml:
apiVersion: v1
kind: Pod
metadata:
  name: config-reader-pod
spec:
  containers:
  - name: my-app
    image: busybox:1.28
    command: [ "sh", "-c", "echo The message is: $(MESSAGE) and the version is $(APP_VERSION) && sleep 3600" ]
    env:
      - name: MESSAGE
        valueFrom:
          configMapKeyRef:
            name: my-app-config # Name of the ConfigMap
            key: MESSAGE       # Key from the ConfigMap's data
      - name: APP_VERSION
        valueFrom:
          configMapKeyRef:
            name: my-app-config
            key: APP_VERSION
  restartPolicy: Never
4. Apply the Podkubectl apply -f config-pod.yaml
5. Verify the ConfigurationCheck the logs of the Pod to see if it correctly read the environment variables from the ConfigMap.kubectl logs config-reader-pod
The output should be:The message is: Hello from a ConfigMap! and the version is v1.1

=======

Project 3: Deploy a Stateful Application with Persistent Storage 💾
Goal: Deploy a simple Redis database using a StatefulSet and a PersistentVolumeClaim (PVC) to ensure its data persists even if the Pod is deleted or rescheduled.
Prerequisites:A Kubernetes cluster with a default StorageClass configured. (Most managed clusters and local tools like Minikube have this by default).
kubectl get storageclass

Steps:1. Create the StatefulSet and Service YAML
This single file defines both the StatefulSet for managing the Redis Pod and a headless Service for stable network identity.Save this content as redis-statefulset.yaml:
apiVersion: v1
kind: Service
metadata:
  name: redis-headless
  labels:
    app: redis
spec:
  ports:
  - port: 6379
    name: redis
  clusterIP: None # This makes it a headless service
  selector:
    app: redis
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis
spec:
  serviceName: "redis-headless"
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:6.2-alpine
        ports:
        - containerPort: 6379
          name: redis
        volumeMounts:
        - name: redis-data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: redis-data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi # Request 1 Gigabyte of storage
2. Apply the StatefulSet and Servicekubectl apply -f redis-statefulset.yaml
3. Verify the DeploymentCheck that the StatefulSet, Pod, and PersistentVolumeClaim were created.# Check the StatefulSet
kubectl get statefulset redis

# Check the Pod (it will have a stable name like redis-0)
kubectl get pod redis-0

# Check the PVC (it will be named based on the volumeClaimTemplates)
kubectl get pvc redis-data-redis-0
You should see that the PVC is in a Bound state.4. Test Data PersistenceLet's write some data to Redis, delete the Pod, and then check if the data is still there.# Get a shell into the redis-0 pod
kubectl exec -it redis-0 -- sh

# Inside the pod, connect to Redis and set a key
# redis-cli
# 127.0.0.1:6379> SET mykey "Hello Persistent World!"
# OK
# 127.0.0.1:6379> GET mykey
# "Hello Persistent World!"
# 127.0.0.1:6379> exit
# exit

# Now, delete the pod from your local terminal
kubectl delete pod redis-0

# Wait for the StatefulSet to automatically recreate the pod
kubectl get pod redis-0 -w # Wait until it's 'Running'

# Get a shell into the NEW redis-0 pod and check for the data
kubectl exec -it redis-0 -- sh

# Inside the new pod, connect to Redis again
# redis-cli
# 127.0.0.1:6379> GET mykey
# "Hello Persistent World!"
The data is still there! This confirms that your Redis instance is using persistent storage managed by the PVC.

============

1) Multi-tier app: NGINX (frontend) → Flask (backend) → MySQL (DB)
What you’ll practice

Namespace, Deployments, Service types, Ingress, ConfigMap, Secret, PVC, StatefulSet, readiness/liveness.

Steps

Create all objects below in order.

Wait for mysql-0 ready, then backend, then frontend.

Hit the Ingress host (or NodePort if you don’t use an Ingress controller).

Test:
kubectl -n shop get pods,svc → open any node’s IP at the frontend NodePort.
====

2) Rolling update + rollback (safely upgrade and undo)
What you’ll practice

Deployment strategy, kubectl rollout, probes, bad release and undo.

Steps

Apply v1.

Update image to a bad tag to trigger failure.

Observe, then rollout undo.

Commands:
# 1) Deploy v1
kubectl apply -f proj2-rolling.yaml
kubectl rollout status deploy/api

# 2) Upgrade to broken tag
kubectl set image deploy/api api=ghcr.io/k8s-demos-mini/hello-api:broken
kubectl rollout status deploy/api --timeout=60s
kubectl describe deploy/api | grep -i "failed" || true

# 3) Roll back
kubectl rollout undo deploy/api
kubectl get rs
=====


3) Blue-Green (switch traffic cleanly)
What you’ll practice

Two versions live, one Service flips selector; optional Ingress.

Steps

Deploy v1 and v2.

Service initially selects v1.

“Cutover” by flipping selector to v2 (atomic traffic switch).

Switch traffic to v2:
kubectl patch svc web -p '{"spec":{"selector":{"app":"web","version":"v2"}}}'
======

4) Autoscaling with HPA
What you’ll practice

Metrics Server dependency, HPA scaling, load generation.

Make sure Metrics Server is installed (most local clusters have it; if not, install per your environment).

Test scaling:
# generate load
kubectl run -it --rm loader --image=busybox -- /bin/sh -c "while true; do wget -qO- http://cpu-app; done"
kubectl get hpa cpu-app -w
================
5) Security: RBAC – least privilege
What you’ll practice

ServiceAccount, Role, RoleBinding, testing permissions.

Test:

# Create a test pod using that SA and try kubectl inside (kubectl image is large; use kubectl via projected token)
POD=$(kubectl run rbac-test --rm -it --image=bitnami/kubectl --serviceaccount=viewer --restart=Never --command -- sh -c "kubectl get pods" | true)
# Alternatively, fetch a token & use curl to the API server (advanced).
========
6) Security: NetworkPolicy – allow only frontend → backend
What you’ll practice

Default deny, allow specific app-to-app traffic, namespaces as boundaries.

Pre-req: Use a CNI that enforces NetworkPolicy (Calico, Cilium, etc.).

Test:
Enter the frontend pod and curl service:
POD=$(kubectl -n np-demo get pod -l app=frontend -o jsonpath='{.items[0].metadata.name}')
kubectl -n np-demo exec -it $POD -- curl -s http://backend
# Try from another random pod in np-demo or default ns -> should be blocked.
=======
7) Pod Security Standards (PSS) via namespace labels
What you’ll practice

Enforcing baseline/restricted, spotting violations.

Steps

Create a namespace with restricted enforcement.

Try to run a privileged pod (should be denied).

Run a compliant pod (works).
Apply: kubectl apply -f proj7-pss.yaml
You’ll see the privileged pod rejected.
==========
This is the most important part. By adding this label to the namespace, you are enforcing the restricted Pod Security Standard on all pods created within this namespace.

The restricted policy is a set of best practices for securing pods. It is designed to enforce highly restrictive security configurations and is recommended for non-privileged applications.

This defines a pod named naughty within the pss-demo namespace.

securityContext: privileged: true

This is the violation. The privileged: true setting gives the container root-level access to the host machine. The restricted Pod Security Standard explicitly forbids privileged containers.

When you try to apply this manifest, the Kubernetes admission controller will check the pss-demo namespace's security policy and block the creation of the naughty pod, returning an error.
=============
