#!/usr/bin/python3
""" start a flask web page """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_text():
    """ Return Hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
