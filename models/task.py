"""Nurse task by doctor"""

from . import db
from models.base import Base


class Task(Base):
    """A nurse's task by the doctor"""

    __tablename__ = "tasks"

    patient_id = db.Column(db.String(100))
    doctor_id = db.Column(db.String(100), nullable=False)
    nurse_id = db.Column(db.String(100))
    description = db.Text
    status = db.Column(db.String(100))
