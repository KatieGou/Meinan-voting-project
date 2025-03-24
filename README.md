### Python formatter and linter
`ruff format && ruff check --fix && pyright`

### Environment setup
Activate virtual env: `source meinan-voting-project/bin/activate`
Deactivate virtual env: `deactivate`

### Docker setup (deprecated)
Run redis image: `docker run -d --name redis-server --network voting-network -p 6379:6379 redis`
Build web docker iamge: `docker build -t meinan-vote-app -f web/Dockerfile .`
Run web docker container: `docker run -p 5000:5000 --network voting-network meinan-vote-app`
Check if an image exists locally: `docker images | grep <image-name>`
Check if a container is running: `docker ps | grep <container-name>`
Stop a container: `docker stop <container-name>`
Remove a container: `docker rm <container-name>`
Remove an image: `docker rmi <image-name>`
Build & run: `docker-compose up --build`
Stop & remove: `docker-compose down`

### Kubernetes setup
MiniKube start: `minikube start`
MiniKube dashboard: `minikube dashboard`
Check if an image exists in minikube: `minikube ssh 'docker images | grep <image-name>'`
Load an image into minikube: minikube image load <image-name>
Access Voting app: `minikube service <service-name>`
