"""User authentication module with sign in and sign up"""
from flask import Blueprint, request, render_template, redirect
from forms import BaseForm, LoginForm
from app import bcrypt
from flask_manager import login_user, logout_user, login_required
from models import Patient, Nurse, Doctor, db


auth = Blueprint('auth', __name__)

def save_profile_pic(image):
    """Saves profile picture"""


@auth.route('/signup', strict_slashes=False, methods=["GET", "POST"])
def signup():
    """Implements user signup logic"""

    form = BaseForm()
    if form.validate_on_submit():
        print(form.data)
        
        return redirect(url_for('auth.login'))
    return redirect(url_for('auth.signup'))


@auth.login('/login', strict_slashes=False, methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pwd = form.password.data
        users = [Patient, Doctor, Nurse]
        for User in users:
            user = User.query.filter_by(email=form.email.data)
            if user and bcrypt.check_hash_password(user.password, pwd):
                login_user(user)
                return "logged in"
        flash("Invalid login credentials", "danger")
    return redirect(url_for("auth.login"))

@auth.logout('/logout', strict_slashes=False)
@login_required
def logout():
    """logs out user"""
    logout_user()
    return "logged out"
