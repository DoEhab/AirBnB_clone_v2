#!/usr/bin/python3
""" start a flask web page """
from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python_text(text="is cool"):
    """ Return input text"""
    return f'Python {escape(text)}'.replace("_", " ")


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_template(n):
    """ Return number """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_number_type(n):
    """ Return number """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
