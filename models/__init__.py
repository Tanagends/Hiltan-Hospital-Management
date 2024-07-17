"""Models"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


doctor_patient = db.Table('doctor_patient',
                          db.Column('doctor_id', db.String(50), db.ForeignKey('doctors.id')),
                          db.Column('patient_id', db.String(50), db.ForeignKey('patients.id'))
                          )

doctor_nurse = db.Table('doctor_nurse',
                        db.Column('doctor_id', db.String(50), db.ForeignKey('doctors.id')),
                        db.Column('nurse_id', db.String(50), db.ForeignKey('nurses.id'))
                        )

nurse_patient = db.Table('nurse_patient',
                         db.Column('nurse_id', db.String(50), db.ForeignKey('nurses.id')),
                         db.Column('patient_id', db.String(50), db.ForeignKey('patients.id'))
                        )

doctor_diagnosis = db.Table('doctor_diagnosis',
                         db.Column('doctor_id', db.String(50), db.ForeignKey('doctors.id')),
                         db.Column('patient_id', db.String(50), db.ForeignKey('diagnosis.id'))
                        )


from models.prescription import Prescription
from models.nurse import Nurse
from models.doctor import Doctor
from models.diagnosis import Diagnosis
from models.patient import Patient
from models.task import Task
from models.booking import Booking
