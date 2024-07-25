"""doctors view"""
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from forms import BookingForm
from models import Booking, db, Task, Diagnosis, Doctor


patient_bp = Blueprint('patient_bp', __name__)


@patient_bp.route('/')
#@login_required
def patient_index():
    """Doctors dashboard"""
    diagnosis = current_user.diagnosis

    current_prescriptions = []
    assigned_doctors = [] + current_user.doctors
    for diag in diagnosis:
        if diag.current == 1:
            current_prescriptions += diag.prescriptions
            doctor = Doctor.query.get(diag.doctor_id)
            if doctor not in assigned_doctors:
                assigned_doctors.append(doctor)

    print(assigned_doctors)
    return render_template('patient_home.html', current_prescriptions=current_prescriptions,
                           assigned_doctors=assigned_doctors)


@patient_bp.route('/booking', methods=["GET", "POST"], strict_slashes=False)
def booking():
    """Patient booking"""

    form = BookingForm()

    if form.validate_on_submit():
        excl_fields = ["csrf_token", "submit"]
        data = {k:v for k,v in form.data.items() if k not in excl_fields}
        data['patient_id'] = current_user.id
        booking = Booking(**data)
        current_user.bookings.append(booking)
        db.session.add(booking)
        db.session.commit()
        flash("Booking Successful", "success")

    bookings = current_user.bookings
    pending_bookings = [b for b in bookings if b.status == "pending"]
    confirmed_bookings = [b for b in bookings if b.status == "booked"]
    done_bookings = [b for b in bookings if b.status == "done"]
    return render_template('patient_booking.html',
                           pending_bookings=pending_bookings,
                           confirmed_bookings=confirmed_bookings,
                           done_bookings=done_bookings,
                           form=form
                           )

@patient_bp.route('/booking/<string:booking_id>/delete', strict_slashes=False)
def delete_booking(booking_id):
    """
       Only the patient can ultimately delete it
    """
    booking = Booking.query.get(booking_id)
    if (doctor := booking.doctor_id):
        doctor.bookings.remove(booking)
    current_user.bookings.remove(booking)
    db.session.delete(booking)
    db.session.commit()
    return render_template(url_for('patient_bp.booking'))

@patient_bp.route('/diagnosis/', strict_slashes=False)
@patient_bp.route('/diagnosis/<string:diag_id>', strict_slashes=False)
def diagnosis(diag_id=None):
    """A patient diagnosis portal, supposed to display a current diagnoses
       And a medical history of past diagnoses
    """
    if diag_id is None:
        diagnosis = current_user.diagnosis
        past_diagnosis = []
        current_diagnosis = []
        for d in diagnosis:
            if d.current == 1:
                current_diagnosis.append(d)
            else:
                past_diagnosis.append(d)

        return render_template('patient_diagnosis.html', past_diagnosis=past_diagnosis, current_diagnosis=current_diagnosis)
    #diagnosis view.... with prescriptions
    diagnosis = Diagnosis.query.get(diag_id)
    prescriptions = diagnosis.prescriptions

    return render_template('patient_single_diagnosis.html', diagnosis=diagnosis, prescriptions=prescriptions)

@patient_bp.route('/prescription', strict_slashes=False)
@patient_bp.route('/prescription/<string:prescription_id>', strict_slashes=False)
def prescriptions(prescription_id=None):
    """A view for all nurses or a single nurse"""

    diagnosis = current_user.diagnosis

    current_prescriptions = []
    past_prescriptions = []
    for diag in diagnosis:
        if diag.current == 1:
            current_prescriptions += diag.prescriptions
        else:
            past_prescriptions += diag.prescriptions
 
    return render_template("patient_prescriptions.html", current_prescriptions=current_prescriptions,
                            past_prescriptions=past_prescriptions)

@patient_bp.route('/prescription/<string:prescription_id>', strict_slashes=False)
#@login_required
def prescription_view(prescription_id):
    """View prescription details"""
    prescription = Prescription.query.get(prescription_id)
    return render_template('patient_prescription_view.html', prescription=prescription)

@patient_bp.route('/doctor/<string:doctor_id>', strict_slashes=False)
#@login_required
def doctor_view(doctor_id):
    """View doctor profile"""
    doctor = Doctor.query.get(doctor_id)
    return render_template('patient_doctor_view.html', doctor=doctor)

