"""Model for a diagnosis"""
from models.base import Base
from . import db
#from models.prescription import Prescription
from models.patient import Patient


class Diagnosis(Base):
    """A medical diagnosis for a patient table model"""

    disease = db.Column(db.String(100))
    description = db.Column(db.String(3000))
    date = db.Column(db.Date)
    cost = db.Column(db.Numeric(10, 2))
    prescriptions = db.relationship('Prescription', backref='diagnosis')
    patient_id = db.Column(db.String(200), db.ForeignKey('patients.id'))
