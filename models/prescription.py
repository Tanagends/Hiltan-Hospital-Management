"""A model for a prescription"""
from models.base import Base


class Prescription(Base):
    """Prescription for a patient by one or more doctors"""

    medicine = db.Column(db.String(3000))
    daily_frequency = db.Column(db.Integer)

