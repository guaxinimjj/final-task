from flask import request
from flask_restful import Resource
from sqlalchemy.sql import func

from department_app.models import db
from department_app.models.departments import Department, Employee
from department_app.models.utils import (
    get_department_by_id,
    set_employees_by_id,
)


class DepartmentsResource(Resource):
    """Resource for departments."""

    def get(self):
        """Get departments."""
        departments = (
            db.session.query(Department)
            .outerjoin(Employee, Department.id == Employee.department_id)
            .group_by(Department.name, Department.id)
            .with_entities(
                Department.id,
                Department.name,
                func.avg(Employee.salary).label("average_salary"),
            )
        )
        return [
            {
                "id": department.id,
                "name": department.name,
                "average_salary": str(department.average_salary),
            }
            for department in departments
        ]

    def post(self):
        """Create new department."""
        name = request.json["name"]
        department = Department(name=name)
        db.session.add(department)
        db.session.commit()
        result = {
            "id": department.id,
            "name": department.name,
        }
        return result, 201


class DepartmentResource(Resource):
    """Resource for department by id."""

    def get(self, department_id):
        """Get department by id."""
        department = get_department_by_id(department_id)
        employees = set_employees_by_id(department_id)
        department_obj = {
            "id": department.id,
            "name": department.name,
            "employees": [
                {
                    "id": employee.id,
                    "name": employee.name,
                    "salary": employee.salary,
                }
                for employee in employees
            ],
        }
        return department_obj, 200

    def put(self, department_id):
        """Update department parameter(s) by id."""
        department = get_department_by_id(department_id)
        department.name = request.json["name"]
        db.session.commit()
        return {}, 200

    def delete(self, department_id):
        """Delete department by id."""
        department = get_department_by_id(department_id)
        db.session.delete(department)
        db.session.commit()
        return {}, 204
