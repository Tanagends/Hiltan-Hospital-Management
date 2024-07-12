"""Model for a diagnosis"""
from models.base import Base
import db


class Diagnosis(Base):
    """A medical diagnosis for a patient table model"""

    disease = db.Column(db.String(100))
    description = db.Column(db.String(3000))
    prescription = db.Column(db.String(3000))
    date = db.Column(db.Date)
    cost = db.Column(db.Numeric(10, 2)
