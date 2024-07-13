"""A nurse model"""
from models.base import DoctorNurseBase
from . import db
from . import nurse_patient


class Nurse(DoctorNurseBase):
    """Models a nurse"""

    __tablename__ = "nurses"

    max_capacity = db.Column(db.Integer, nullable=False)
    patients = db.relationship('Patient', secondary=nurse_patient, backref='nurses')
