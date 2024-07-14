"""User authentication module with sign in and sign up"""
from flask import Blueprint, request, render_template, redirect, url_for
from forms import BaseForm, LoginForm
from flask_login import login_user, logout_user, login_required
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
        print("yes")
        return redirect(url_for('auth.login'))
    else:
        print("no")
        return render_template('signup.html', form=form)


@auth.route('/login', strict_slashes=False, methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pwd = form.password.data
        users = [Patient, Doctor, Nurse]
        for User in users:
            user = User.query.filter_by(email=form.email.data)
            from app import bcrypt
            if user and bcrypt.check_hash_password(user.password, pwd):
                login_user(user)
                return "logged in"
        flash("Invalid login credentials", "danger")
    return render_template("login.html", form=form)

@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    """logs out user"""
    logout_user()
    return "logged out"
