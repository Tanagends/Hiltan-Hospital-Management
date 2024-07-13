#!/usr/bin/env python3
"""The Hiltan Hospital Management Application"""
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://hiltan_admin:hiltan_pwd@localhost/hiltan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', strict_slashes=False)
def index():
    """Landing page"""
    return "Welcome to Hiltan Hospital"

if __name__ == "__main__":
    with app.app_context():
        from models import Patient, Doctor, Nurse, Prescription, Diagnosis
        db.create_all()
    app.run(debug=True)
