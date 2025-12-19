import os
from models import db
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import select, or_, and_

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///'{os.path.join(basedir, 'data/'}"

db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run('0.0.0.0', 5001, debug=True)
