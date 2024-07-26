# Hiltan Hospital Application

## Overview

Hiltan Hospital Application is a comprehensive healthcare management system designed to streamline patient care, diagnosis, and treatment processes. The application integrates digital treatment and consultation services for patients, doctors, and nurses, enhancing the efficiency and quality of healthcare delivery.

## Key Functionality

### Patient View
- **Dashboard:** View current prescriptions and assigned doctors.
- **Booking:** Schedule and manage appointments with doctors.
- **Diagnosis:** Access current and past medical diagnoses.
- **Prescriptions:** View current and past prescriptions.
- **Doctor Profile:** View detailed profiles of assigned doctors.

### Doctor View
- **Dashboard:** Access all assigned patients and their details.
- **Patient Management:** View and update patient information.
- **Diagnosis & Prescription:** Create and manage diagnoses and prescriptions for patients.

### Nurse View
- **Dashboard:** View current tasks assigned by doctors, along with related doctors and patients.
- **Patient Management:** Access details of current and past patients.
- **Task Management:** View and complete tasks assigned by doctors.
- **Schedule Management:** Update availability status.

## Setup and Installation

### Prerequisites

- Python 3.7+
- Virtual Environment

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Tanagends/Hiltan-Hospital-Management.git
   cd Hiltan-Hospital-Management
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**
   Ensure you have a PostgreSQL/MySQL database set up and update the database URI in the `config.py` file.
   ```python
   SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/hiltan_hospital'
   ```

5. **Initialize Database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application**
   ```bash
   flask run
   ```

7. **Access the Application**
   Open your browser and go to `http://127.0.0.1:5000`.

## Directory Structure

```
hiltan-hospital/
│
├── app/
│   ├── templates/
│   │   ├── doctor/
│   │   ├── nurse/
│   │   ├── patient/
│   │   └── layouts/
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── models/
│   │   ├── base.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── nurse.py
│   │
│   ├── routes/
│   │   ├── doctor.py
│   │   ├── nurse.py
│   │   └── patient.py
│   │
│   ├── forms/
│   │   ├── booking_form.py
│   │   ├── prescription_form.py
│   │   └── diagnosis_form.py
│   │
│   ├── __init__.py
│   ├── config.py
│   └── app.py
│
├── migrations/
│
├── env/
│
├── requirements.txt
│
├── README.md
│
└── run.py
```

## Key Files

- **app.py:** Entry point of the Flask application.
- **config.py:** Configuration file for the application.
- **requirements.txt:** List of all dependencies required by the application.
- **migrations/**: Folder containing database migration scripts.

## Usage

- **Activate Virtual Environment:**
  ```bash
  source env/bin/activate
  ```

- **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

- **Run the Application:**
  ```bash
  flask run
  ```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Coding!
