from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@postgres-server:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    count = db.Column(db.Integer, nullable=False)


@app.route("/")
def index():
    animals = Animal.query.all()
    return {
        animal.name: animal.count
        for animal in animals
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
