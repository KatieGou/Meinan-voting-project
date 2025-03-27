from flask import Flask, render_template, request, jsonify
import redis
import logging
import os
import time
from config import config, configure_logging

configure_logging()

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")
app_config = config[env]

redis_client = redis.Redis(
    host=app_config.REDIS_HOST,
    port=app_config.REDIS_PORT,
    decode_responses=app_config.DECODE_RESPONSES,
)


def wait_for_redis():
    retries = 5
    while retries > 0:
        try:
            redis_client.ping()
            logging.info("Connected to Redis")
            break
        except redis.ConnectionError as e:
            logging.error(e)
            logging.warning("Could not connect to Redis. Retrying...")
            time.sleep(3)
            retries -= 1
    if retries == 0:
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
    app.run(host=app_config.FLASK_HOST, port=5000, debug=app_config.DEBUG)
