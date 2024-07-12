"""The patient model"""
from models.base import BasePerson


class Patient(BasePerson):
    """Models a table of patients"""

    __tablename__ = 'patients'

    state = db.Column(db.String(250))
