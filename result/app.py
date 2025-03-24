from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
app = Flask(__name__)

username = os.getenv("PGUSER", "postgres")
password = os.getenv("PGPASSWORD", "postgres")
host = os.getenv("PGHOST", "postgres-service")
port = os.getenv("PGPORT", 5432)
database = os.getenv("PGDATABASE", "postgres")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{username}:{password}@{host}:{port}/{database}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Votes(db.Model):
    __tablename__ = "votes"
    id = db.Column("id", db.Integer, primary_key=True)
    animal_name = db.Column("animal", db.String(255), unique=True, nullable=False)
    count = db.Column("count", db.Integer, nullable=False)


@app.route("/")
def index():
    animals = Votes.query.all()
    votes = {animal.animal_name: animal.count for animal in animals}

    total_votes = sum(votes.values())
    percent_votes = {
        animal: (count / total_votes) * 100 for animal, count in votes.items()
    }

    sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))
    winner = list(sorted_votes.keys())[0] if sorted_votes else "No votes yet"
    return render_template(
        "index.html",
        votes=sorted_votes,
        total_votes=total_votes,
        percent_votes=percent_votes,
        winner=winner,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
