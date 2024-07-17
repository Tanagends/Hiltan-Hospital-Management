"""doctors view"""
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from models import Patient, Doctor, Nurse, Prescription, Diagnosis, Booking, Task


doctor_bp = Blueprint('doctor_bp', __name__)


@doctor_bp.route('/', strict_slashes=False)
#@login_required
def doctor_index():
    """Doctors dashboard"""
    patients = Patients.qeury.limit(6).all()
    recent_diagnosis = Diagnosis.query.order_by(Diagnosis.date_created.desc()).limit(3)
    pending_bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                       filter(Booking.status == "pending").all()


    return render_template('doctor_home.html')

@doctor_bp.route('/patients', strict_slashes=False)
def all_patients():
    """View for all patients"""
    patients = Patients.qeury.all()

@doctor_bp.route('/booking', strict_slashes=False)
def booking():
    """accept bookings which move to the Schedule section"""


@doctor_bp.route('/diagnosis/<string:patient_id>', strict_slashes=False)
def diagnosis(patient_id):
    """A patient diagnosis portal"""
    patient = Patient.query.get(patient_id)
