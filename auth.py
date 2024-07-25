"""User authentication module with sign in and sign up"""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from forms import BaseForm, LoginForm
from flask_login import login_user, logout_user, login_required
from models import Patient, Nurse, Doctor, db
import os
from uuid import uuid4
from werkzeug.utils import secure_filename


auth = Blueprint('auth', __name__)


def save_profile_pic(image):
    """Saves profile picture"""
    if not image:
        return
    _, ext = os.path.splitext(image.filename)
    filenam = os.path.join(str(uuid4()) + ext)
    filename = secure_filename(filenam)
    filepath = os.path.join('static/images', filename)
    try:
        image.save(filepath)
        return os.path.join('/', filepath)
    except Exception as e:
        print('Saving failed')
        print(e)
        return None

@auth.route('/signup', strict_slashes=False, methods=["GET", "POST"])
def signup():
    """Implements user signup logic"""

    form = BaseForm()
    if form.validate_on_submit():
        users = {'doctor': Doctor, 'nurse': Nurse, 'patient': Patient}
        excl = ['csrf_token', 'role', 'confirm_password', 'password',
                'profile_pic', 'submit']
        data = {k: v.strip() if isinstance(v, str) else v for k, v 
                in form.data.items() if k not in excl}

        from app import bcrypt
        data['password'] = bcrypt.generate_password_hash(form.password.data)
        if pic := form.profile_pic.data:
            data['profile_pic'] = save_profile_pic(pic)

        user = users[form.role.data](**data)

        db.session.add(user)
        db.session.commit()
        flash("Signup successful", "success")

        return redirect(url_for('auth.login'))
    else:

        return render_template('sig2.html', form=form)


@auth.route('/login', strict_slashes=False, methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pwd = form.password.data
        users = [Patient, Doctor, Nurse]
        print('yes')
        for User in users:
            user = User.query.filter_by(email=form.email.data).all()
            from app import bcrypt
            if user and bcrypt.check_password_hash(user[0].password, pwd.strip()):
                login_user(user[0])
                flash("Login successful", "success")
                if Doctor.query.get(user[0].id):
                    return redirect(url_for("doctor_bp.doctor_index"))
                elif Patient.query.get(user[0].id):
                    return redirect(url_for("patient_bp.patient_index"))
                else:
                    return redirect(url_for("nurse_bp.nurse_index"))
        form.password.errors.append("Invalid login details")
    return render_template("log.html", form=form)


@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    """logs out user"""
    logout_user()
    flash("logout success", "success")
    return render_template("land2.html")
