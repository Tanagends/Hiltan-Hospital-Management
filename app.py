#!/usr/bin/env python3
"""The Hiltan Hospital Management Application"""
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://hiltan_admin:hiltan_pwd@localhost/hiltan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tanatswa'
#csrf = CSRFProtect(app)


from models import db
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

login_manager.login_view = 'login'

from models import Patient, Doctor, Nurse, Prescription, Diagnosis
@login_manager.user_loader
def load_user(user_id):
    """Loads a user"""
    users = [Patient, Doctor, Nurse]
    for User in users:
        user = User.query.get(user_id)
        if user:
            return user
    return None
from auth import auth
from views.nurse import nurse_bp
from views.patient import patient_bp
from views.doctor import doctor_bp
app.register_blueprint(auth)
app.register_blueprint(nurse_bp, url_prefix='/nurse')
app.register_blueprint(doctor_bp, url_prefix='/doctor')
app.register_blueprint(patient_bp, url_prefix='/patient')

@app.route('/', strict_slashes=False)
def index():
    """Landing page"""
    return render_template('landing.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
