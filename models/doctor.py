"""A model for the doctor"""
from models.base import DoctorNurseBase
from . import db, doctor_nurse, doctor_patient, doctor_diagnosis


class Doctor(DoctorNurseBase):
    """Model for doctors"""

    __tablename__ = "doctors"

    specialty = db.Column(db.String(50))
    tasks = db.relationship('Task', backref='doctor')
    bookings = db.relationship('Booking', backref='doctor')
    own_tasks = db.relationship('DoctorTask', backref='doctor')
    nurses = db.relationship('Nurse', secondary=doctor_nurse, backref=('doctors'))
    patients = db.relationship('Patient', secondary=doctor_patient, backref=('doctors'))
    diagnosis = db.relationship('Diagnosis', secondary=doctor_diagnosis, backref=('doctors'))
