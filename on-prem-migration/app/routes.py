from flask import render_template
from app import db
from app.models import Employee
from flask import current_app as app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees')
def list_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)
