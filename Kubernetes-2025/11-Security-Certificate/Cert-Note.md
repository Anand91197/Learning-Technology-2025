# 1. Generate a private key for anand
openssl genrsa -out anand.key 2048

# 2. Create a CSR for anand, specifying the user's name and group
openssl req -new -key anand.key -subj "/CN=anand/O=devs" -out anand.csr

# anand-csr.yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: anand-access
spec:
  request: <PASTE_BASE64_ENCODED_CSR_HERE>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth




cat anand.csr | base64 | tr -d '\n'


kubectl apply -f anand-csr.yaml
kubectl certificate approve anand-access


kubectl get csr anand-access -o jsonpath='{.status.certificate}' | base64 --decode > anand.crt


Create the Kubeconfig File
Now, you'll create a kubeconfig file that "anand" can use to connect to the cluster. This file bundles the cluster's API server address, the CA certificate, and "anand's" new key and certificate.


# 1. Define the cluster context
kubectl config set-cluster kubernetes-cluster --server=<YOUR_API_SERVER_ADDRESS> --certificate-authority=<PATH_TO_YOUR_CLUSTER_CA_CERT> --embed-certs=true --kubeconfig=anand-kubeconfig

# 2. Set user credentials
kubectl config set-credentials anand --client-key=anand.key --client-certificate=anand.crt --embed-certs=true --kubeconfig=anand-kubeconfig

# 3. Create a new context linking the cluster and user
kubectl config set-context anand-context --cluster=kubernetes-cluster --user=anand --kubeconfig=anand-kubeconfig

# 4. Set the new context as the current one in the file
kubectl config use-context anand-context --kubeconfig=anand-kubeconfig


3. Configure RBAC (Role-Based Access Control)
By default, "anand" has no permissions. You need to create Role and RoleBinding or ClusterRole and ClusterRoleBinding to grant them specific access rights.

Grant Access to a Specific Namespace (e.g., dev)
This is the most common use case. You give "anand" access only to resources within a designated namespace.

# anand-dev-role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: anand-dev-role
  namespace: dev
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: anand-dev-rolebinding
  namespace: dev
subjects:
- kind: User
  name: anand # Must match the CN from the CSR
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: anand-dev-role
  apiGroup: rbac.authorization.k8s.io





  Grant Cluster-Wide Read-Only Access
If you want to give "anand" read-only access to all resources in the cluster, you can use a built-in ClusterRole like view.


# anand-view-clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: anand-view-clusterrolebinding
subjects:
- kind: User
  name: anand # Must match the CN from the CSR
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: rbac.authorization.k8s.io

  After creating these YAML files, apply them to grant "anand" the defined permissions.


  # Network Policy

The podSelector targets the database pod through its label.
The policyTypes field specifies that only ingress traffic is affected.
The ingress rule allows traffic specifically from pods with the label name: api-pod on TCP port 3306.



If no ingress rules are specified, Kubernetes treats the policy as a complete block for incoming traffic.

