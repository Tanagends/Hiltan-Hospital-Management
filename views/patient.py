"""doctors view"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from forms import BookingForm


patient_bp = Blueprint('patient_bp', __name__)


@patient_bp.route('/')
#@login_required
def patient_index():
    """Doctors dashboard"""
    diagnosis = current_user.diagnosis

    current_prescriptions = []
    for diag in diagnosis:
        if diag.current == 1:
            current_prescriptions += diag.prescriptions
    assigned_doctors = current_user.doctors
    
    return render_template('patient_home.html', current_prescriptions=current_prescriptions,
                           assignd_doctors=assigned_doctors)


@patient_bp.route('/booking')
def booking():
    """Patient booking"""

    form = BookingForm()

    if form.validate_on_submit():
        logic for saving a booking

    return render_template('nurse_booking.html')


@patient_bp.route('/diagnosis/', strict_slashes=False)
def diagnosis(patient_id=None):
    """A patient diagnosis portal"""
    if patient_id is None:
        diagnosis = doctor.diagnosis
        return render_template('all_diagnosis.html', diagnosis=diagnosis)
    #diagnosis form
    patient = Patient.query.get(patient_id)
    diagnosis = patient.diagnosis

    return render_template('doctor_diagnosis.html', patient=patient, diagnosis=diagnosis)

@patient_bp.route('/nurses', strict_slashes=False)
@patient_bp.route('/nurses/<string:nurse_id>', strict_slashes=False)
def nurses(nurse_id=None):
    """A view for all nurses or a single nurse"""
    
    if nurse_id is None:
        nurses = Nurse.query.filter(Nurse.availability == 1).all()
        return render_template("all_nurses.html", nurses=nurses)

    else:
        nurse = Nurse.query.get(nurse_id)
        return render_template("single_nurse.html")

