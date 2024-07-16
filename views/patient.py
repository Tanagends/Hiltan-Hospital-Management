"""doctors view"""
from flask import Blueprint, render_template
from flask_login import login_required


patient_bp = Blueprint('patient_bp', __name__)


#@patient_bp.route('/')
@login_required
def patient_index():
    """Doctors dashboard"""
    return render_template('patient_home.html')
