#requires -version 3
minikube.exe docker-env | Invoke-Expression
#docker build -t hello-node:0.0.1 .
docker build -t hello-node:0.0.2 .

