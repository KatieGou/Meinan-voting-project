from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from config import config, configure_logging

configure_logging()

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")
app.config.from_object(config[env])

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
    app.run(host=app.config["FLASK_HOST"], debug=app.config["DEBUG"], port=5001)
