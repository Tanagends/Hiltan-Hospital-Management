"""nurse's view"""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from models import db, Task, Doctor, Patient


nurse_bp = Blueprint('nurse_bp', __name__)


@nurse_bp.route('/', strict_slashes=False)
#@login_required
def nurse_index():
    """Nurse's dashboard"""
    tasks = current_user.tasks
    current_tasks = [t for t in tasks if t.status == "pending"]
    current_doctors = [Doctor.query.get(t.doctor_id) for t in current_tasks]
    current_patients = [Patient.query.get(t.patient_id) for t in current_tasks]

    return render_template('nurse_home.html', current_tasks=current_tasks,
                           current_doctors=current_doctors,
                           current_patients=current_patients
                           )


@nurse_bp.route('/patients', strict_slashes=False)
def patient():
    """showspast and current patients"""

    tasks = current_user.tasks
    current_tasks = [t for t in tasks if t.status == "pending"]
    past_tasks = [t for t in tasks if t.status == "completed"]
    current_patients = [Patient.query.get(t.patient.id) for t in current_tasks]
    past_patients = [Patient.query.get(t.patient.id) for t in past_tasks]

    return render_template("nurse_patients.html", current_patients=current_patients,
                           past_patients=past_patients)

@nurse_bp.route('/tasks/<string:task_id>', strict_slashes=False)
@nurse_bp.route('/tasks', strict_slashes=False)
def task(task_id=None):
    """Tasks, completed and present"""
    if task_id is not None:
        task = Task.query.get(task_id)
        task.status = "completed"
        db.session.commit()
        return redirect(url_for('nurse_bp.task'))
    #else mark task completed
    tasks = current_user.tasks
    current_tasks = [t for t in tasks if t.status == "pending"]
    past_tasks = [t for t in tasks if t.status == "completed"]
    return render_template("nurse_tasks.html", current_tasks=current_tasks,
                           past_tasks=past_tasks)
                            
#route for marking task completion

@nurse_bp.route('/schedule/<int:signal>')
def schedule(signal):
    """Updates schedule"""
    nurse = Nurse.query.get(current_user)
    nurse.availability = signal
    db.session.commit()

    return render_template('nurse_home.html')
