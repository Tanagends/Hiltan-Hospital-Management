"""Model for a diagnosis"""
from models.base import Base
from . import db
#from models.prescription import Prescription
from models.patient import Patient


class Diagnosis(Base):
    """A medical diagnosis for a patient table model"""

    disease = db.Column(db.String(50))
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    prescriptions = db.relationship('Prescription', backref='diagnosis')
    patient_id = db.Column(db.String(50), db.ForeignKey('patients.id'))
    current = db.Column(db.Integer, default=1)
