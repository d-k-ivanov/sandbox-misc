#requires -version 3

minikube.exe docker-env | Invoke-Expression

kubectl delete service hello-node
kubectl delete deployment hello-node

docker rmi hello-node:0.0.1 hello-node:0.0.2 -f 

minikube.exe docker-env -u | Invoke-Expression

