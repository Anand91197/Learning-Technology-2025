Step:1 Created on the Worker Node: 


sudo mkdir -p /tmp/data/my-app-data
sudo chmod 777 /tmp/data/my-app-data # Adjust permissions as needed
echo "Hello from kube-node-1!" | sudo tee /tmp/data/my-app-data/file1.txt


Step 2: Define the PersistentVolume (PV)

Step 3: Define the PersistentVolumeClaim (PVC)

Step 4: Mount the PVC in a Pod

Step 5: Demonstrate Persistence
Execute into the Pod and create a test file in the mounted path:

kubectl exec -it nginx-pv-deployment-6d9cb88686-hxdxc  -- sh
echo "Hello Persistent World!" > /app/data/persistent-test.html

kubectl port-forward nginx-pv-deployment-6d9cb88686-hxdxc 8080:80
Then, in a new terminal: (Master)
curl http://localhost:8080/persistent-test.html

Now, Delete the Nginx Pod. The Deployment will automatically create a new one.
What I found, the directory present /app/data, with single file1.txt, which only created on the Node-1

Step 6: Clean Up (IMPORTANT for Retain Policy)
Because we used persistentVolumeReclaimPolicy: Retain, you must delete resources in a specific order.


kubectl delete -f nginx-with-pv.yaml
kubectl delete -f my-pvc.yaml
kubectl delete -f my-pv.yaml

