# Meinan Voting Project

## Project Overview
This project is a voting application built with Flask, Redis, and PostgreSQL. It allows users to vote for their favorite animals and view the results in real-time.

## Prerequisites
- Python 3.9+
- Docker
- Docker Compose
- Kubernetes (Minikube or any other Kubernetes cluster)
- `pre-commit` (for code formatting and linting)

## Environment Setup
1. **Create and activate a virtual environment:**
    ```sh
    python -m venv meinan-voting-project
    source meinan-voting-project/bin/activate
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Deactivate the virtual environment:**
    ```sh
    deactivate
    ```

## Running the Application Locally
1. **Build the images:**
    ```sh
    docker-compose build
    ```
2. **Start Minikube:**
    ```sh
    minikube start
    ```
3. **Load the images into Minikube:**
    ```sh
    minikube image load <image-name>
    ```
4. **Deploy the application:**
    ```sh
    kubectl apply -f k8s/
    ```
5. **Access the application:**
    ```
    minikube service <service-name>
    ```
6. **Stop Minikube:**
    ```sh
    minikube stop
    ```
7. **Delete the application:**
    ```sh
    kubectl delete -f k8s/
    ```

## Helpful Commands

### Python formatter and linter
- `ruff format && ruff check --fix`

### Docker
- Run redis image: `docker run -d --name redis-server --network voting-network -p 6379:6379 redis`
- Build web docker iamge: `docker build -t web-image -f web/Dockerfile .`
- Run web docker container: `docker run -p 5000:5000 --network voting-network web-image`
- Check if an image exists locally: `docker images | grep <image-name>`
- Check if a container is running: `docker ps | grep <container-name>`
- Stop a container: `docker stop <container-name>`
- Remove a container: `docker rm <container-name>`
- Remove an image: `docker rmi <image-name>`
- Remove all untagged images: `docker image prune --filter="dangling=true"`
- Build & run: `docker-compose up --build`
- Stop & remove: `docker-compose down`

### Kubernetes
- MiniKube start: `minikube start`
- MiniKube dashboard: `minikube dashboard`
- Check if an image exists in minikube: `minikube ssh 'docker images | grep <image-name>'`
- Load an image into minikube: minikube image load <image-name>
- Access Voting app via a browser: `minikube service <service-name>`
- Port-Forward the PostgreSQL Service: `kubectl port-forward svc/postgres-service 5432:5432`
- Get services, pods, deployments: `kubectl get svc,pods,deploy`
- Get logs: `kubectl logs <pod-name>`
- Delete all: `kubectl delete all --all`
- Delete a specific resource: `kubectl delete <resource> <resource-name>`

### Helm
- Install Helm: `brew install helm`
`helm list`
`helm install meinan-voting-app ./meinan-voting-app`
`helm uninstall meinan-voting-app`
