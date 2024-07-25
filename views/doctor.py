"""doctors view"""
from flask import Blueprint, render_template, abort, url_for, redirect
from flask_login import login_required, current_user
from models import db, Patient, Doctor, Nurse, Prescription, Diagnosis, Booking, Task, DoctorTask
from forms import TaskForm, DiagnosisForm, DoctorTaskForm

#Add the delete account for all
#code a flash card and style for feedback throughout the app


doctor_bp = Blueprint('doctor_bp', __name__)


@doctor_bp.route('/', strict_slashes=False, methods=["GET", "POST"])
#@login_required
def doctor_index():
    """Doctors dashboard"""
    form = DoctorTaskForm()
    patients = current_user.patients
    patients = patients if len(patients) <= 3 else patients[0:3]
    #diagnosis = Diagnosis.query.order_by(Diagnosis.date_created.desc()).limit(3)
    bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked")
    tasks = current_user.own_tasks
    return render_template('doctor_home.html', patients=patients, tasks=tasks,
                           bookings=bookings, form=form)
    
    #Booking options are pending(doctor's approval), booked, done
    #return render_template('doctor_home.html')

@doctor_bp.route('/patients', strict_slashes=False)
@doctor_bp.route('/patients/<string:patient_id>/remove', strict_slashes=False)
def all_patients(patient_id=None):
    """View for all patients"""
    patients = current_user.patients
    if patient_id is None:
        return render_template('doctor_patients.html', patients=patients)
    else:
        patient = Patient.query.get(patient_id)
        current_user.patients.remove(patient)
        db.session.commit()
        return render_template('doctor_patients.html', patients=patients)

@doctor_bp.route('/patients/remove/<string:patient_id>/', strict_slashes=False)
def home_patients(patient_id=None):
    """home patients"""
    patient = Patient.query.get(patient_id)
    current_user.patients.remove(patient)
    db.session.commit()
    return redirect(url_for("doctor_bp.doctor_index"))

@doctor_bp.route('/patients/<string:patient_id>', strict_slashes=False)
def single_patient(patient_id):
    """A view for a single patient"""
    pass


@doctor_bp.route('/bookings', strict_slashes=False)
@doctor_bp.route('/bookings/<string:booking_id>', strict_slashes=False)
def booking(booking_id=None):
    """accept bookings which move to the Schedule section"""

    if booking_id is not None:
        booking = Booking.query.get(booking_id)
        booking.doctor_id = current_user.id
        booking.status = 'booked'
        current_user.bookings.append(booking)
        patient = Patient.query.get(booking.patient_id)
        current_user.patients.append(patient)
        db.session.commit()

    pending_bookings = Booking.query.filter(Booking.status == "pending").all()
    my_bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                    filter(Booking.status == "booked").all()
    past_bookings = Booking.query.filter(Booking.doctor_id == current_user.id).\
                                filter(Booking.status == "booked").all()

    return render_template('doctor_bookings.html', my_bookings=my_bookings,
                           pending_bookings=pending_bookings, past_bookings=past_bookings)

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

@doctor_bp.route('/bookings/<string:booking_id>/done', strict_slashes=False)
def done_bookings(booking_id):
    """Bookings that are done"""

    booking = Booking.query.get(booking_id)
    booking.status = 'done'
    db.session.commit()
    return render_template(url_for('doctor_bp.booking'))

@doctor_bp.route('/diagnosis/<string:patient_id>/create', strict_slashes=False, methods=["GET", "POST"])
@doctor_bp.route('/diagnosis/', strict_slashes=False)
def diagnosis(patient_id=None):
    """ A patient diagnosis portal: renders all doctors diagnosis
        When patient_id is passed, it allows a doctor to diagnose a patient
        Each diagnosis has a prescribe button which leads to a prescription
        for that diagnosis
    """
    if patient_id is None:
        diagnosis = current_user.diagnosis
        return render_template('doctor_diagnosis.html', diagnosis=diagnosis)
    #diagnosis form
    form = DiagnosisForm()
    patient = Patient.query.get(patient_id)
    if form.validate_on_submit():
        excl_fields = ['csrf_token', 'submit']
        data ={k:v for k, v in form.data.items() if k not in excl_fields}
        data['patient_id'] = patient_id
        data['doctor_id'] = current_user.id
        new_diagnosis = Diagnosis(**data)
        current_user.diagnosis.append(new_diagnosis)
        patient = Patient.query.get(patient_id)
        patient.diagnosis.append(new_diagnosis)
        if patient not in current_user.patients:
            current_user.patients.append(patient)
        db.session.add(new_diagnosis)
        db.session.commit()

        return redirect(url_for('doctor_bp.diagnosis'))
    return render_template('doctor_form_diagnosis.html', patient=patient, form=form)

@doctor_bp.route('/diagnosis/<string:diagnosis_id>/view', strict_slashes=False, methods=["GET", "POST"])
def diagnosis_view(diagnosis_id):
    """A view of diagnosis and its prescriptions"""
    diagnosis = Diagnosis.query.get(diagnosis_id)
    prescriptions = diagnosis.prescriptions
    return render_template('diagnosis_prescriptions.html', diagnosis=diagnosis, prescriptions=prescriptions)

@doctor_bp.route('/diagnosis/<string:diag_id>/delete', strict_slashes=False)
def delete_diagnosis(diag_id):
    """Deletes a diagnosis from everyone and its related prescriptions
       It's a button on each diagnosis
    """
    diagnosis = Diagnosis.query.get(diag_id)
    prescriptions = diagnosis.prescriptions
    for p in prescriptions:
        diagnosis.prescriptions.remove(p)
        db.session.delete(p)
    current_user.diagnosis.remove(diagnosis)
    patient = Patient.query.get(diagnosis.patient_id)
    patient.diagnosis.remove(diagnosis)
    db.session.delete(diagnosis)
    db.session.commit()
    return render_template(url_for('doctor_bp.diagnosis'))

@doctor_bp.route('/diagnosis/<string:diag_id>/toggle_not_current', strict_slashes=False)
def toggle_diagnosis(diag_id):
    """
    Toggles a diagnosis not current, medical history
    """
    diagnosis = Diagnosis.query.get(diag_id)
    diagnosis.current = 0
    
    db.session.commit()
    return render_template(url_for('doctor_bp.diagnosis'))



@doctor_bp.route('/prescription/<string:diag_id>', strict_slashes=False, methods=["GET", "POST"])
@doctor_bp.route('/prescription/', strict_slashes=False, methods=["GET", "POST"])
def prescription(diag_id=None):
    """All my prescriptions, the button at the top but not nav of the diagnoses template.
       which leads to all prescriptions view
       If a diagnoses id is passed, make a prescription through a form
       Every prescription also has a view diagnosis, which leads to a single diadnoses view and its
       accompanying prescriptions
    """
    if diag_id is None:
        prescriptions = []
        diag = current_user.diagnosis
        for d in diag:
            prescriptions += d.prescriptions
        return render_template("doctor_prescriptions.html", prescriptions=prescriptions)
    form = PrescriptionForm()
    if form.validate_on_submit() and diag_id is not None:
        excl_fields = ['csrf_token', 'submit']
        data ={k:v for k, v in form.data.items() if k not in excl_fields}
        data['diagnosis_id'] = diag_id
        new_prescription = Prescription(**data)
        diagnosis = Diagnosis.query.get(diag_id)
        diagnosis.prescriptions.append(new_prescription)
        db.session.add(new_prescription)
        db.session.commit()
        return redirect(url_for('doctor_bp.prescription'))

    return render_template('doctor_prescription_form.html', form=form)

@doctor_bp.route('/prescription/<string:prescription_id>/delete', strict_slashes=False)
def delete_prescription(prescription_id):
    """Deletes a prescription, a button that appears on every prescription
    """
    prescription = Prescription.query.get(prescription_id)
    diagnosis = prescription.diagnosis
    diagnosis.prescriptions.remove(prescription)
    db.session.delete(prescription)
    db.session.commit()
    return render_template(url_for('doctor_bp.prescription'))



@doctor_bp.route('/nurses', strict_slashes=False, methods=["GET", "POST"])
@doctor_bp.route('/nurses/<string:task_id>/remove', strict_slashes=False)
def nurses(task_id=None):
    """A view for all nurses or and my nurse"""
    
    if task_id is None:
        nurses = Nurse.query.filter(Nurse.availability == 1).limit(3).all()
        tasks = current_user.tasks
        return render_template("doctor_nurses.html", nurses=nurses, tasks=tasks)

    else:
        task = Task.query.get(task_id)
        current_user.tasks.remove(task)
        nurse = task.nurse
        nurse.tasks.remove(task)
        db.session.delete(task)

        doc_tasks = False
        for task in nurse.tasks:
            if task.doctor_id == current_user.id:
                doc_tasks = True
        if not doc_tasks:
            current_user.nurses.remove(nurse)

        db.session.commit()
        return redirect(url_for("doctor_bp.nurses"))




@doctor_bp.route('/nurses/<string:nurse_id>', strict_slashes=False, methods=["GET", "POST"])
def assign_nurse(nurse_id):
    """Assigns a nurse"""
    form = TaskForm()
    if form.validate_on_submit():
        excl_fields = ['csrf_token', 'submit']
        data = {k:v for k, v in form.data.items() if k not in excl_fields}
        data['doctor_id'] = current_user.id
        new_task = Task(**data)
        nurse = Nurse.query.get(nurse_id)
        nurse.tasks.append(new_task)
        if nurse not in current_user.nurses:
            current_user.nurses.append(nurse)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("doctor_bp.nurses"))
    return render_template('nurse_assignment.html', form=form)

@doctor_bp.route('/tasks', strict_slashes=False, methods=["GET", "POST"])
@doctor_bp.route('/tasks/<string:task_id>', strict_slashes=False, methods=["GET", "POST"])
def task(task_id=None):
    """Tasks - Home page code"""
    form = DoctorTaskForm()
    if form.validate_on_submit() and task_id is None:
        new_task = DoctorTask(description=form.data.get('description'),
                   doctor_id=current_user.id)
        current_user.own_tasks.append(new_task)
        db.session.add(new_task)
        db.session.commit()

    else:
        task = DoctorTask.query.get(task_id)
        current_user.own_tasks.remove(task)
        db.session.delete(task)
        db.session.commit()

    return redirect(url_for("doctor_bp.doctor_index"))

@doctor_bp.route('/tasks/<string:task_id>', strict_slashes=False)
def task_done(task_id):
    """done tasks"""
    task = DoctorTask.query.get(task_id)
    task.status = "completed"
    db.session.commit()
    return redirect(url_for("doctor_bp.doctor_index"))
