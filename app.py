from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import select, or_, and_

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0', 5001, debug=True)
