"""A model for a prescription"""
from models.base import Base
from . import db
from models.diagnosis import Diagnosis


class Prescription(Base):
    """Prescription for a patient by one or more doctors"""

    medicine = db.Column(db.String(50))
    disease = db.Column(db.String(50))
    instruction = db.Column(db.Text)
    start_date = db.Column(db.Date)
    finish_date = db.Column(db.Date)
    dosage = db.Column(db.String(50))
    diagnosis_id = db.Column(db.String(50), db.ForeignKey('diagnosis.id'))
