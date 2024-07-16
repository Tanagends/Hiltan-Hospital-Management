"""Booking for a patient"""

from . import db
from models.base import Base


class Booking(Base):
    """Patient-Doctor booking model"""

    __tablename__ = "bookings"

    patient_id = db.Column(db.String(100), nullable=False)
    doctor_id = db.Column(db.String(100))
    note = db.Text
    status =  db.Column(db.String(100))
