"""Doctor's task"""
from . import db
from models.base import Base


class DoctorTask(Base):
    """Doctor's own Task"""

    __tablename__ = "doctor_tasks"

    doctor_id = db.Column(db.String(100), db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.String(100), db.ForeignKey('patients.id'))
    description =db.Column(db.Text)
    due = db.Column(db.DateTime)
