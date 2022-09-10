from distutils.log import debug
from email.policy import default
from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:////tmp/testtodo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/name')
def print_name():
    return "Hello, Ayush. Welcome to the world of python. We're sure you'll love it"


@app.route('/page')
def print_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)