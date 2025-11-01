# Project: Monitoring Stack with kube-prometheus-stack (Helm)

1. Pre-requisites

Helm installed

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version


Metrics Server installed (for autoscaling & resource metrics):

kubectl get deployment metrics-server -n kube-system


If missing, install:

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

2. Add the Helm repo & update
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

3. Create a namespace for monitoring
kubectl create namespace monitoring

4. Install kube-prometheus-stack
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring


This installs:

Prometheus

Alertmanager

Grafana

Node Exporter

kube-state-metrics

5. Verify all pods
kubectl get pods -n monitoring


You should see pods for Prometheus, Grafana, Alertmanager, etc.

6. Access Grafana Dashboard

Get Grafana admin password:

kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 -d ; echo


Port-forward Grafana service:

kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80


Open http://localhost:3000
 → Login:

Username: admin

Password: (output from above command)

You’ll see pre-built Kubernetes/Node dashboards 🎉

7. Access Prometheus UI
kubectl port-forward svc/monitoring-kube-prometheus-prometheus -n monitoring 9090:9090


Open http://localhost:9090
.

8. Access Alertmanager UI
kubectl port-forward svc/monitoring-kube-prometheus-alertmanager -n monitoring 9093:9093


Open http://localhost:9093
.

9. Add Custom Grafana Dashboards (Optional)

In Grafana → “Dashboards” → “Import” → paste IDs from Grafana.com:

Kubernetes cluster monitoring: 315

Node Exporter full: 1860

10. Add a Custom Alert Rule (example)

Create a PrometheusRule to alert if a node’s CPU > 80% for 5 minutes.

apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: high-cpu
  namespace: monitoring
spec:
  groups:
  - name: node.rules
    rules:
    - alert: HighNodeCPU
      expr: 100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High CPU usage detected on node {{ $labels.instance }}"
        description: "Node CPU usage > 80% for 5m"


Apply it:

kubectl apply -f cpu-alert.yaml

🔍 What You Learned Here

Helm-based app installation

Monitoring (Prometheus, Grafana)

Alerting with PrometheusRule

Port-forward & Grafana dashboards

Metrics (kube-state-metrics, Node Exporter)

