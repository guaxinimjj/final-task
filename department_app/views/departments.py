from flask import render_template, request, redirect, url_for
from sqlalchemy.sql import func, or_, and_
from department_app.models.departments import Department, db, Employee


def index():
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


def department(id):
    department = Department.query.get(id)
    employees = Employee.query.filter_by(department_id=id)
    if request.method == "POST":
        department.name = request.form["name"]
        try:
            db.session.commit()
            return redirect(url_for("department", id=id))
        except:
            return "Something go wrong!"
    elif request.method == "DELETE":
        db.session.delete(department)
        db.session.commit()
    return render_template(
        "department.jinja2", department=department, employees=employees
    )


def get_employee_query(where=None):
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


def get_search_query(args):
    if not any(args.values()):
        # workaround for filter method when `true` is not supported
        return Employee.id is not None

    name = args.get("name")
    date_from = args.get("date_from")
    date_by = args.get("date_by")

    query = None
    if date_from and date_by:
        query = and_(
            Employee.date_birth >= date_from,
            Employee.date_birth <= date_by,
        )
    elif date_from:
        query = Employee.date_birth >= date_from
    elif date_by:
        query = Employee.date_birth <= date_by

    if name:
        name_query = Employee.name.ilike(f"%{name}%")
        if query is not None:
            query = or_(
                query,
                name_query,
            )
        else:
            query = name_query
    return query


def employees_search():
    departments = Department.query.all()
    where = get_search_query(request.args)
    query = get_employee_query(where)
    employees = query.all()
    return render_template(
        "employees.jinja2", employees=employees, departments=departments
    )


def employee(id):
    departments = Department.query.all()
    where = Employee.id == id
    query = get_employee_query(where)
    employee = query.one()

    if request.method == "POST":
        employee.name = request.form["name"]
        employee.date_birth = request.form["date_birth"]
        employee.salary = request.form["salary"]
        employee.department_id = request.form["depart_name"]
        try:
            db.session.commit()
            return redirect(url_for("employee", id=id))
        except:
            return "Something go wrong!"
    elif request.method == "DELETE":
        db.session.delete(employee)
        db.session.commit()

    return render_template("employee.jinja2", employee=employee, departments=departments)
