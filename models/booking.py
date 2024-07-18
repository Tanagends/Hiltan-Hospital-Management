"""Booking for a patient"""

from . import db
from models.base import Base


class Booking(Base):
    """Patient-Doctor booking model"""

    __tablename__ = "bookings"

    patient_id = db.Column(db.String(100), db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.String(100), db.ForeignKey('doctors.id'))
    note = db.Text
    status =  db.Column(db.String(100))
