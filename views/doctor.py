"""doctors view"""
from flask import Blueprint, render_template, abort, url_for
from flask_login import login_required, current_user
from models import Patient, Doctor, Nurse, Prescription, Diagnosis, Booking, Task
from forms import TaskForm

#Add the delete account for all
#code a flash card and style for feedback throughout the app


doctor_bp = Blueprint('doctor_bp', __name__)


@doctor_bp.route('/', strict_slashes=False)
#@login_required
def doctor_index():
    """Doctors dashboard
    patients = Doctor.query.get(current_user.id).patients
    patients = patients if len(patients) <= 3 else patients[0:3]
    diagnosis = Diagnosis.query.order_by(Diagnosis.date_created.desc()).limit(3)
    bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked")

    return render_template('doctor_home.html', patients=patients, diagnosis=diagnosis,
                           bookings=bookings)
    """
    #Booking options are pending(doctor's approval), booked, done
    return render_template('doctor_home.html')

@doctor_bp.route('/patients', strict_slashes=False)
@doctor_bp.route('/patients/<string: patient_id>', strict_slashes=False)
def all_patients(patient_id=None):
    """View for all patients"""
    if patient_id is None:
        patients = current_user.patients
        return render_template('doctor_patients.html', patients=patients)
    else:
        patient = Patient.query.get(patient_id)
        return render_template('doctor_single_patient.html', patient=patient)


@doctor_bp.route('/bookings', strict_slashes=False)
@doctor_bp.route('/bookings/<string:booking_id>', strict_slashes=False)
@doctor_bp.route('/bookings/<string:booking_id>/delete', strict_slashes=False)
def booking(booking_id=None):
    """accept bookings which move to the Schedule section"""

    if booking_id is not None:
        booking = Booking.query.get(booking_id)
        booking.doctor_id = current_user.id
        booking.status = 'booked'
        current_user.bookings.append(booking)
        db.session.commit()

    pending_bookings = Booking.query.filter(Booking.status == "pending").all()
    my_bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked").all()

    return render_template('doctor_bookings.html', my_bookings=my_bookings,
                           pending_bookings=pending_bookings)

@doctor_bp.route('/bookings/<string:booking_id>/delete', strict_slashes=False)
def delete_booking(booking_id):
    """Deletes a booking from being the doctor's, to pending
       Only the patient can ultimately delete it
    """
    booking = Booking.query.get(booking_id)
    booking.status = 'pending'
    booking.doctor_id = None
    current_user.bookings.remove(booking)
    db.session.commit()
    return render_template(url_for('doctor_bp.booking'))


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

@doctor_bp.route('/nurses', strict_slashes=False, methods=["GET", "POST"])
@doctor_bp.route('/nurses/<string:nurse_id>', strict_slashes=False)
def nurses(nurse_id=None):
    """A view for all nurses or a single nurse"""
    
    if nurse_id is None:
        form = TaskForm()
        nurses = Nurse.query.filter(Nurse.availability == 1).limit(3).all()
        #my_nurses = current_user.nurses
        if form.validate_on_submit():
            excl_fields = []
            data = {k:v for k, v in form.data.items() if k not in excl_fields}
            new_task = Task(**data)
            nurse = Nurse.query.get(form.data.nurse_id)
            nurse.tasks.append(new_task)
            current_user.nurses.append(nurse)
            db.session.add(new_task)
            db.session.commit()
        return render_template("doctor_nurses.html", nurses=nurses)#my_nurses=my_nurses

    else:
        nurse = Nurse.query.get(nurse_id)
        return render_template("doctor_single_nurse.html", nurse=nurse)

@doctor_bp.route('/tasks', strict_slashes=False)
@doctor_bp.route('/tasks/task_id', strict_slashes=False)
def task(task_id=None):
    """Tasks - Home page code
    form = DoctorTaskForm()
    if form.validate_on_submit() and task_id is None:
        excl_fields = []
        data = {k:v for k, v in form.data if k not in excl_fields}
        new_task = DoctorTask(**data)
        current_user.tasks.append(new_task)
        db.session.add(new_task)
        db.session.commit()

    else:
        task = DoctorTask.query.get(task_id)
        current_user.tasks.remove(task)
        db.session.delete(task)
        db.session.commit()

    return render_template('doctor_home.html')
    """
