#!/usr/bin/python3
""" start a flask web page """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_text():
    """ Return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_text(text):
    """ Return input text"""
    return f'C {escape(text)}'.replace("_", " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
