"""A model for the doctor"""
from models.base import DoctorNurseBase


class Doctor(DoctorNurseBase):
    """Model for doctors"""

    __tablename__ = "doctors"

    specialty = db.Column(db.String(100))
