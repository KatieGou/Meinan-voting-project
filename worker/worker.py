import redis
import psycopg2
import time
import logging
import os
from config import config, configure_logging

configure_logging()

env = os.getenv("FLASK_ENV", "development")
app_config = config[env]
redis_client = redis.Redis(
    host=app_config.REDIS_HOST,
    port=app_config.REDIS_PORT,
    decode_responses=app_config.DECODE_RESPONSES,
)

# Define global variables for database connection
conn = None
cur = None


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
    if retries == 0:
        raise Exception("Could not connect to Redis")


def wait_for_postgres():
    global conn, cur
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname=app_config.DB_NAME,
                user=app_config.DB_USER,
                password=app_config.DB_PASSWORD,
                host=app_config.DB_HOST,
                port=app_config.DB_PORT,
            )
            cur = conn.cursor()
            logging.info("Connected to PostgreSQL")
            break
        except psycopg2.OperationalError:
            logging.warning("Could not connect to PostgreSQL. Retrying...")
            time.sleep(3)
            retries -= 1
    if retries == 0:
        raise Exception("Could not connect to PostgreSQL")


wait_for_redis()
wait_for_postgres()


cur.execute("""
CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    animal VARCHAR(255) NOT NULL UNIQUE,
    count INT NOT NULL
)
""")
conn.commit()


def transfer_votes():
    while True:
        votes = {
            animal: int(redis_client.get(animal)) for animal in redis_client.keys()
        }
        for animal, count in votes.items():
            if count:
                logging.info(f"Transferring {count} votes for {animal}")
                cur.execute(
                    """
                INSERT INTO votes (animal, count) 
                    VALUES (%s, %s)
                    ON CONFLICT (animal)
                    DO UPDATE SET count = votes.count + EXCLUDED.count
                """,
                    (animal, count),
                )
                conn.commit()
                redis_client.set(animal, 0)
        time.sleep(10)


if __name__ == "__main__":
    logging.info("Starting worker...")
    transfer_votes()
