#requires -version 3

minikube addons enable heapster
kubectl get po,svc -n kube-system
minikube addons open heapster

