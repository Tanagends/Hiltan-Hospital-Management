"""The patient model"""
from models.base import BasePerson
from . import db
from models import doctor_patient
#from models.diagnosis import Diagnosis


class Patient(BasePerson):
    """Models a table of patients"""

    __tablename__ = 'patients'

    state = db.Column(db.String(50))
    diagnosis = db.relationship('Diagnosis', backref='patient')
    nurse_tasks = db.relationship('Task', backref='patient')
    bookings = db.relationship('Booking', backref='patient')
#    doctors = db.relationship('Doctor', secondary=doctor_patient, back_populates='patients')
