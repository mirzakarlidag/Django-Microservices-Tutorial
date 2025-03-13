from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/main"
CORS(app)

db = SQLAlchemy(app)


class Producy(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route("/")
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
