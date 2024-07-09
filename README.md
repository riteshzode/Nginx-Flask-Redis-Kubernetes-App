# Nginx-Flask-Redis-Kubernetes-App

### Try With Kubernetes

#### To start the application

Step 1: Apply the deployment in folder `my-k8s-app`

    kubectl apply -f .

Step 2: List deployment and services

    kubectl get all -A

Step 3: Delete deployment and services

    kubectl delete -f .

Step 4: Port forward nginx to localhost or you can try LoadBalancer

    kubectl port-forward svc/nginx 8080:8080

## Docker
  A Docker image for this project is available on Docker Hub at ```riteshzode/flaskapp:v3```. To run the application using Docker:


### Pull the Docker image with three versions v1, v2, v3:
  
  Copy code
  ```riteshzode/flaskapp:v3```

#### Repository Link - https://hub.docker.com/r/riteshzode/flaskapp/tags
