"""All Base Models"""
from datetime import datetime
from . import db
from uuid import uuid4
from flask_login import UserMixin


class Base(UserMixin, db.Model):
    """Base for all classes"""

    __abstract__ = True

    id = db.Column(db.String(50), primary_key=True, default=str(uuid4()))
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_modified = db.Column(db.DateTime, onupdate=db.func.now())


class BasePerson(Base):
    """Base classes for the doctor, patient and nurse"""

    __abstract__ = True

    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(50))
    profile_pic = db.Column(db.String(50))
    address = db.Column(db.String(200))


class DoctorNurseBase(BasePerson):
    """Common fields for doctors and nurses"""

    __abstract__ = True

    shift_start = db.Column(db.Time)
    shift_end = db.Column(db.Time)
    experience = db.Column(db.Date)
