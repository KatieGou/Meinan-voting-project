Activate virtual env: `source meinan-voting-project/bin/activate`
Deactivate virtual env: `deactivate`
Run redis image: `docker run -d --name redis-server --network voting-network -p 6379:6379 redis`
Run frontend: `docker run -p 5000:5000 --network voting-network meinan-vote-app`
Python formatter and linter: `ruff format && ruff check --fix && pyright`