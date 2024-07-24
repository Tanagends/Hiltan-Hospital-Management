"""doctors view"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from forms import BookingForm
from models import Booking, db, Task


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


@patient_bp.route('/booking', methods=["GET", "POST"], strict_slashes=False)
def booking():
    """Patient booking"""

    form = BookingForm()

    if form.validate_on_submit():
        excl_fields = []
        data = {k:v for k,v in form.data.items() if k not in excl_fields}
        #ensure patient_id is included
        booking = Booking(**data)
        patient.bookings.append(booking)
        db.session.add(booking)
        db.session.commit()

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
    """Deletes a booking from being the doctor's, to pending
       Only the patient can ultimately delete it
    """
    booking = Booking.query.get(booking_id)
    if (doctor := booking.doctor_id == None):
        doctor.bookings.remove(booking)
    current_user.bookings.remove(booking)
    db.session.delete(booking)
    db.session.commit()
    return render_template(url_for('patient_bp.booking'))

@patient_bp.route('/diagnosis/', strict_slashes=False)
@patient_bp.route('/diagnosis/<string:diag_id>', strict_slashes=False)
def diagnosis(diag_id=None):
    """A patient diagnosis portal"""
    if diag_id is None:
        diagnosis = current_user.diagnosis
        past_diagnosis = []
        current_diagnosis = [d if diagnosis.current == 1 else past_diagnosis.append(d) for d in diagnosis]

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
