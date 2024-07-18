"""nurse's view"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import db


nurse_bp = Blueprint('nurse_bp', __name__)


@nurse_bp.route('/')
#@login_required
def nurse_index():
    """Doctors dashboard"""
    nurse = Nurse.query.get(current_id.id)
    doctors = nurse.doctors
    tasks = nurse.tasks

    return render_template('nurse_home.html')


@nurse_bp.route('/schedule/<int:signal>')
def schedule(signal):
    """Updates schedule"""
    nurse = Nurse.query.get(current_user)
    nurse.availability = signal
    db.session.commit()

    return render_template('nurse_home.html')
