"""User authentication module with sign in and sign up"""
from flask import Blueprint, request, render_template, redirect
from forms import BaseForm
from app import bcrypt


auth = Blueprint('auth', __name__)


@auth.route('/signup', strict_slashes=False, methods=["GET", "POST"])
def signup():
    """Implements user signup logic"""

    form = BaseForm()
    if form.validate_on_submit():
        print(form.data)
        return redirect(url_for('login'))
    return redirect(url_for('signup'))


@auth.login('/login', strict_slashes=False, methods=["GET", "POST"])
def login():
    pass

@auth.logout(/'logout', strict_slashes=False)
def logout()
