"""Nurse task by doctor"""

from . import db
from models.base import Base


class Task(Base):
    """A nurse's task by the doctor"""

    __tablename__ = "tasks"

    patient_id = db.Column(db.String(100), db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.String(100), db.ForeignKey('doctors.id'), nullable=False)
    nurse_id = db.Column(db.String(100), db.ForeignKey('nurses.id'))
    description = db.Text
    status = db.Column(db.String(100), default='pending') #completed
