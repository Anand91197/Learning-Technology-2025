Installation of the ArgoCD

1. Install Argo CD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


kubectl get pods -n argocd


2. Creating the NodePort Service for the ArgoCD UI
argocd-server-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: argocd-server-nodeport
  namespace: argocd
spec:
  type: NodePort
  ports:
    - name: http
      port: 80
      targetPort: 8080
      nodePort: 30080
    - name: https
      port: 443
      targetPort: 8080
      nodePort: 30443
  selector:
    app.kubernetes.io/name: argocd-server

Apply it with kubectl apply -f argocd-server-nodeport.yaml

Access the WEB UI: http://<worker-node-ip>:30080

3. Get Initial Admin Password

kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d

======
echo "# Argocd-gitops-sample-app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Testingbyme0011/Argocd-gitops-sample-app.git
git push -u origin main


===
# Connect GitHub Repo in Argo CD

argocd login localhost:8080 \
  --username admin \
  --password <YOUR_PASSWORD> \
  --insecure

argocd repo add https://github.com/Testingbyme0011/Argocd-gitops-sample-app.git

=====
# Create Argo CD Application
Argocd-gitops-sample-app.yaml
kubectl apply -f Argocd-gitops-sample-app.yaml

kubectl get pods,svc -n default -o wide

=====