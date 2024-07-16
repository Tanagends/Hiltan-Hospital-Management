"""doctors view"""
from flask import Blueprint, render_template
from flask_login import login_required


doctor_bp = Blueprint('doctor_bp', __name__)


@doctor_bp.route('/')
#@login_required
def doctor_index():
    """Doctors dashboard"""
    return render_template('doctor_home.html')
