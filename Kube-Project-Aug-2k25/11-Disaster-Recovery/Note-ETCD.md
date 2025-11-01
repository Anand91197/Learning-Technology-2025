Disaster Recovery: etcd backup & restore (kubeadm “stacked” etcd)
What you’ll practice

Safe snapshot, validating, and restoring.

Run these on a control-plane node where etcd runs as a static pod (/etc/kubernetes/manifests/etcd.yaml).

Backup (snapshot)
export ETCDCTL_API=3
ETCDCTL="etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key"
$ETCDCTL snapshot save /root/etcd-snap-$(date +%F-%H%M).db
$ETCDCTL snapshot status /root/etcd-snap-*.db


Restore (to a fresh data dir)
# Stop kubelet to stop static pods
sudo systemctl stop kubelet

# Move old data aside
sudo mv /var/lib/etcd /var/lib/etcd.bak.$(date +%s)

# Restore snapshot into a new dir
sudo ETCDCTL_API=3 etcdctl snapshot restore /root/etcd-snap-YYYY-MM-DD-HHMM.db \
  --data-dir=/var/lib/etcd

# Start kubelet; it will recreate the etcd static pod using the new data dir
sudo systemctl start kubelet

# Verify cluster comes up; check etcd & kube-apiserver pods
kubectl -n kube-system get pods -l component=etcd -o wide

How to use this pack

Save each project YAML to its own file and apply with kubectl apply -f <file>.

Watch pods: kubectl get pods -A -w.

Clean up: kubectl delete -f <file>.
====================================