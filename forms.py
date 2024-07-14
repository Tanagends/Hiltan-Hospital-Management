from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DateField, SubmitField, BooleanField, SelectField, PasswordField, RadioField, TimeField, IntegerField
from wtforms.validators import InputRequired, Email, ValidationError, DataRequired, Length, EqualTo
from datetime import date
from models import Doctor, Nurse, Patient


class BaseForm(FlaskForm):
    """Base form for doctor. nurse and patient signup"""

    choices = [('patient', 'Patient'), ('doctor', 'Doctor'),
               ('nurse', 'Nurse')]

    name = StringField('Name', validators=[DataRequired(),
                                           Length(min=2, max=20)])
    surname = StringField('surname', validators=[DataRequired(),
                                                 Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    gender = RadioField('Gender assigned at birth',
                        choices=['Male', 'Female'], validators=[DataRequired()])
    address = StringField('Physical Address', validators=[Length(max=300)])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    profile_pic = FileField('Upload Profile Picture', validators=[FileAllowed(
                            ['jpg', 'jpeg', 'png', 'gif', 'ico'])])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=
                                     [DataRequired(), EqualTo
                                     ('password',
                                     message='Passwords must match')])
    role = SelectField('Role', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

    @property
    def age(self):
        """Calculates the age of the user"""
        today = date.today()

        if self.dob:
            age = today.year - self.dob.year
            if ((today.month, today.day) <  (self.dob.month, self.dob.day)):
                age = -1
            return age
        return None

    def validate_email(self, email):
        """Vaiidates that email is already not in use"""
        users = [Patient, Doctor, Nurse]

        for User in users:
            user = User.query.filter_by(email=email.data).all()
            if user:
                raise ValidationError("Email already in use. Please login")


class DoctorNurseForm(BaseForm):
    """Doctors and Nurses Fields"""
    shift_start = TimeField('Shift starting time')
    shift_end = TimeField('Shift ending time')
    experience = DateField('Career starting year')

    @property
    def years_of_experience(self, career_start):
        """Years of experience"""
        today = date.today()
        if self.career_start.data:
            return (today.year - self.career_start)
        return None


class DoctorForm(DoctorNurseForm):
    """Doctors Sign up form"""
    specialty = StringField('Specialty')


class NurseForm(DoctorNurseForm):
    """Nurse Signup Form"""
    max_capacity = BooleanField('Are you already assigned maximum patients')


class PatientForm(BaseForm):
    """Patients form"""


class LoginForm(FlaskForm):
    """Login form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
