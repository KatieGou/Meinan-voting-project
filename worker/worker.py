import redis
import psycopg2
import time
import logging

logging.basicConfig(level=logging.INFO)

redis_client = redis.Redis(host="redis-server", port=6379, decode_responses=True)
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="postgres-server",
    port="5432",
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    animal VARCHAR(255) NOT NULL,
    count INT NOT NULL
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
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
                    "INSERT INTO votes (animal, count) VALUES (%s, %s)", (animal, count)
                )
                conn.commit()
                redis_client.set(animal, 0)
        time.sleep(10)


if __name__ == "__main__":
    logging.info("Starting worker...")
    transfer_votes()
