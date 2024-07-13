"""A model for a prescription"""
from models.base import Base
from . import db
from models.diagnosis import Diagnosis


class Prescription(Base):
    """Prescription for a patient by one or more doctors"""

    medicine = db.Column(db.String(3000))
    disease = db.Column(db.String(200))
    instruction = db.Column(db.Text)
    start_date = db.Column(db.Date)
    finish_date = db.Column(db.Date)
    dosage = db.Column(db.String(db.String(1000)))
    diagnosis_id = db.Column(db.String(200), db.ForeignKey('diagnosis.id'))
