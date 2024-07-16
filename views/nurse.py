"""nurse's view"""
from flask import Blueprint, render_template
from flask_login import login_required


nurse_bp = Blueprint('nurse_bp', __name__)


@nurse_bp.route('/')
#@login_required
def nurse_index():
    """Doctors dashboard"""
    return render_template('nurse_home.html')
