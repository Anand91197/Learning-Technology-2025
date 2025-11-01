Deploy a StatefulSet with 3 MongoDB pods

1. Mongo-headless-service.yaml

2. Mongo-statefulset.yaml

kubectl apply -f mongo-headless-service.yaml
kubectl apply -f mongo-statefulset.yaml
