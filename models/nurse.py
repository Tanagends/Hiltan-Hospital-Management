"""A nurse model"""
from models.base import DoctorNurseBase
from . import db
from models import nurse_patient, doctor_nurse


class Nurse(DoctorNurseBase):
    """Models a nurse"""

    __tablename__ = "nurses"

    availability = db.Column(db.Integer, nullable=False, default=1)
    patients = db.relationship('Patient', secondary=nurse_patient, backref='nurses')
    tasks = db.relationship('Task', backref='nurse')
#    doctors = db.relationship('Doctor', secondary=doctor_nurse, back_populates='nurses')

