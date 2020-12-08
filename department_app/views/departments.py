from flask import render_template, request, redirect, url_for
from sqlalchemy.sql import func
from department_app.models.departments import Department, db, Employee
from department_app.models.utils import get_search_query


def index():
    """Index page, display a list departments, and average salary. Create new department."""

    departments = (
        db.session.query(Department)
        .outerjoin(Employee, Department.id == Employee.department_id)
        .group_by(Department.name, Department.id)
        .with_entities(
            Department.id,
            Department.name,
            func.avg(Employee.salary).label("average_salary"),
        )
    ).all()
    if request.method == "POST":
        name = request.form["name"]
        add_departmens = Department(name=name)
        try:
            db.session.add(add_departmens)
            db.session.commit()
            return redirect(url_for("index"))
        except:
            return "Something go wrong!"
    else:
        return render_template("departments.jinja2", departments=departments)


def department(department_id):
    """Department page, display a list employees. Update or delete department."""
    department = Department.query.get(department_id)
    employees = Employee.query.filter_by(department_id=department_id)
    if request.method == "POST":
        department.name = request.form["name"]
        try:
            db.session.commit()
            return redirect(url_for("department", id=department_id))
        except:
            return "Something go wrong!"
    elif request.method == "DELETE":
        db.session.delete(department)
        db.session.commit()
    return render_template(
        "department.jinja2", department=department, employees=employees
    )


def get_employee_query(where=None):
    """Query for employees page."""
    query = (
        db.session.query(Employee)
        .outerjoin(Department, Department.id == Employee.department_id)
        .with_entities(
            Department.name.label("department_name"),
            Employee.id,
            Employee.name,
            Employee.date_birth,
            Employee.salary,
            Employee.department_id,
        )
    )
    if where is None:
        return query

    return query.filter(where)


def employees():
    """Employees page, show all employees. Add new employee."""
    department = Department.query.all()
    query = get_employee_query()
    employees = query.all()
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        salary = request.form["salary"]
        department_name = request.form["depart_name"]
        add_emploee = Employee(
            name=name, department_id=department_name, date_birth=date, salary=salary
        )
        try:
            db.session.add(add_emploee)
            db.session.commit()
            return redirect(url_for("department", id=department_name))
        except:
            return "Something go wrong!"

    return render_template(
        "employees.jinja2", employees=employees, departments=department
    )


def employees_search():
    """Employees search."""
    departments = Department.query.all()
    where = get_search_query(request.args)
    query = get_employee_query(where)
    employees = query.all()
    return render_template(
        "employees.jinja2", employees=employees, departments=departments
    )


def employee(employee_id):
    """Employee page. Update or delete employee."""
    departments = Department.query.all()
    where = Employee.id == employee_id
    query = get_employee_query(where)
    employee = query.one()

    if request.method == "POST":
        employee.name = request.json["name"]
        employee.date_birth = request.json["date_birth"]
        employee.salary = request.json["salary"]
        employee.department_id = request.json["depart_name"]
        try:
            db.session.commit()
            return redirect(url_for("employee", id=employee_id))
        except:
            return "Something go wrong!"
    return render_template("employee.jinja2", employee=employee, departments=departments)
