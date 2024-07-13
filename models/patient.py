"""The patient model"""
from models.base import BasePerson
from . import db
#from models.diagnosis import Diagnosis


class Patient(BasePerson):
    """Models a table of patients"""

    __tablename__ = 'patients'

    state = db.Column(db.String(250))
    diagnosis = db.relationship('Diagnosis', backref='patient')
