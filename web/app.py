from flask import Flask, render_template, request, jsonify
import redis
import logging
import os
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)


def wait_for_redis():
    retries = 5
    while retries > 0:
        try:
            redis_client.ping()
            logging.info("Connected to Redis")
            break
        except redis.ConnectionError:
            logging.warning("Could not connect to Redis. Retrying...")
            time.sleep(3)
            retries -= 1
    raise Exception("Could not connect to Redis")


def initialize_votes():
    default_votes = {"cats": 0, "dogs": 0, "birds": 0, "fish": 0}
    for animal, count in default_votes.items():
        if redis_client.get(animal) is None:
            redis_client.set(animal, count)


wait_for_redis()
initialize_votes()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    animal = data.get("animal", "").lower()

    if redis_client.exists(animal):
        redis_client.incr(animal)
        return jsonify({"message": "Vote successful", "your_vote": animal})
    else:
        return jsonify({"message": "Invalid animal", "your_vote": "None"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
