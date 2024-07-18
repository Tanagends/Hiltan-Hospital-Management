"""doctors view"""
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from models import Patient, Doctor, Nurse, Prescription, Diagnosis, Booking, Task
from forms import TaskForm


doctor_bp = Blueprint('doctor_bp', __name__)


@doctor_bp.route('/', strict_slashes=False)
#@login_required
def doctor_index():
    """Doctors dashboard
    patients = Doctor.query.get(current_user.id).patients
    patients = patients if len(patients <= 3) else patients[0:3]
    diagnosis = Diagnosis.query.order_by(Diagnosis.date_created.desc()).limit(3)
    bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked")

    return render_template('doctor_home.html', patients=patients, diagnosis=diagnosis,
                           bookings=bookings)
    """
    return render_template('doctor_home.html')

@doctor_bp.route('/patients', strict_slashes=False)
def all_patients():
    """View for all patients"""
    patients = Doctor.query.get(current_user.id).patients

    return render_template('all_patients.html', patients=patients)

@doctor_bp.route('/booking', strict_slashes=False)
@doctor_bp.route('/booking/<string:booking_id>', strict_slashes=False)
def booking(booking_id=None):
    """accept bookings which move to the Schedule section"""
    if booking_id is not None:
        pending_bookings = Booking.query.filter(Booking.status == "pending").all()
        booking = Booking.query.get(booking_id)
        booking.doctor_id = current_user.id
        booking.status = 'booked'
        db.session.commit()

    pending_bookings = Booking.query.filter(Booking.status == "pending").all()
    my_bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked")

    return render_template('doctor_bookings.html', my_bookings=my_bookings, 
                           pending_bookings=pending_bookings)

@doctor_bp.route('/diagnosis/<string:patient_id>', strict_slashes=False)
@doctor_bp.route('/diagnosis/', strict_slashes=False)
def diagnosis(patient_id=None):
    """A patient diagnosis portal"""
    if patient_id is None:
        diagnosis = doctor.diagnosis
        return render_template('all_diagnosis.html', diagnosis=diagnosis)
    #diagnosis form
    patient = Patient.query.get(patient_id)
    diagnosis = patient.diagnosis

    return render_template('doctor_diagnosis.html', patient=patient, diagnosis=diagnosis)

@doctor_bp.route('/nurses', strict_slashes=False)
@doctor_bp.route('/nurses/<string:nurse_id>', strict_slashes=False)
def nurses(nurse_id=None):
    """A view for all nurses or a single nurse"""
    
    if nurse_id is None:
        nurses = Nurse.query.filter(Nurse.availability == 1).all()
        return render_template("all_nurses.html", nurses=nurses)

    else:
        nurse = Nurse.query.get(nurse_id)
        return render_template("single_nurse.html")

@doctor_bp.route('/task', strict_slashes=False)
@doctor_bp.route('/task/task_id', strict_slashes=False)
def task(task_id=None):
    """Tasks"""
    form = TaskForm()
    if form.validate_on_submit():
        """Adding logic + nurse append"""

    return render_template('doctor_task.html')
