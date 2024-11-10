# Nginx-Flask-Redis-Kubernetes-App

### Try With Kubernetes

## Install NGINX Ingress Controller - [View Documentation on GitHub](https://github.com/kubernetes/ingress-nginx)

Step 1: Create the ingress-nginx Namespace

    kubectl create namespace ingress-nginx

Step 2: Install the Ingress Controller

    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.0-beta.0/deploy/static/provider/cloud/deploy.yaml

Step 3: Verify the Installation
Check that the NGINX Ingress Controller is running by verifying the pods and services:

    kubectl get all -n ingress-nginx

That's it! You've installed the NGINX Ingress Controller using kubectl.

#### To start the application

Step 1: Apply the deployment in folder `my-k8s-app-with-ingres`

    kubectl apply -f .

Step 2: List deployment and services

    kubectl get all -A

Step 3: Delete deployment and services

    kubectl delete -f .

Step 4: Port forward nginx to localhost or you can try LoadBalancer

    kubectl port-forward svc/web 5000:5000

Step 5: List ingress

    kubectl get ingress

## Docker
  A Docker image for this project is available on Docker Hub at ```riteshzode/flaskapp:v3```. To run the application using Docker:


### Pull the Docker image with three versions v1, v2, v3:
  
  Copy code
  ```riteshzode/flaskapp:v3```

#### Repository Link - https://hub.docker.com/r/riteshzode/flaskapp/tags
