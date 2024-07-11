#!/usr/bin/env python3
"""The Hiltan Hospital Management Application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Landing page"""
    return "Welcome to Hiltan Hospital"

if __name__ == "__main__":
    app.run(debug=True)
