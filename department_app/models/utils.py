from sqlalchemy.sql import or_, and_

from department_app.models import db
from department_app.models.departments import Department, Employee


def get_departments() -> list:
    """Query to get all Department."""
    return Department.query.all()


def get_department_by_id(department_id):
    """Query to get Department by id."""
    return Department.query.get(department_id)


def get_employee_by_id(employee_id):
    """Query to get Employee by id."""
    where = Employee.id == employee_id
    query = get_employee_query(where)
    return query.one()


def set_department_by_id(department_id):
    """Query to get Department filter by id."""
    return Department.query.filter(id=department_id).one()


def set_employees_by_id(department_id):
    """Query to get Employee filter by id."""
    return Employee.query.filter_by(department_id=department_id)


def get_employee_query(where=None):
    """Query for employees for search."""
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


def get_search_query(args):
    """Get search parameters."""
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
