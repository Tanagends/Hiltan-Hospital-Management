"""A nurse model"""
from models.base import DoctorNurseBase
import db


class Nurse(DoctorNurseBase):
    """Models a nurse"""

    __tablename__ = "nurses"
