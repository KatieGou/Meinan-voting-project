# Meinan Voting Project

## Project Overview
This project is a voting application built with Flask, Redis, and PostgreSQL. It allows users to vote for their favorite animals and view the results in real-time.

## Prerequisites
- Python 3.9+
- Docker
- Docker Compose
- Kubernetes (Minikube or any other Kubernetes cluster)
- `pre-commit` (for code formatting and linting)
- Helm (for Kubernetes package management)

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
3. **Point the shell to minikube's docker-daemon:**
    ```sh
    eval $(minikube -p minikube docker-env)
    ```
4. **Build the images within minikube's docker-daemon:**
    ```sh
    docker compose build
    ```
5. **Deploy the Application:**
    ```sh
    helm upgrade --install meinan-voting-app ./meinan-voting-app
    ```
6. **Access the application:**
    ```sh
    minikube service meinan-voting-app-result-service
    minikube service meinan-voting-app-web-service
    ```
    The application should now be accessible in your browser.
7. **Stop Minikube:**
    ```sh
    minikube stop
    ```
8. **Delete the application:**
    ```sh
    helm delete meinan-voting-app
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
- Point your shell to minikube's docker-daemon: `eval $(minikube -p minikube docker-env)`
- Rebuild all images: `docker-compose build`
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
- List Helm releases: `helm list`
- Deploy a Helm chart: `helm install <release-name> <chart-path>`
- Uninstall a Helm release: `helm uninstall <release-name>`
- Upgrade a Helm release: `helm upgrade <release-name> <chart-path>`
- Rollback a Helm release: `helm rollback <release-name> <revision>`
- Get Helm release history: `helm history <release-name>`
- Get Helm release status: `helm status <release-name>`