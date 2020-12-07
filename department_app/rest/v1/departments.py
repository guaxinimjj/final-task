from flask import request
from flask_restful import Resource
from sqlalchemy.sql import func

from department_app.models import db
from department_app.models.departments import Department, Employee


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
                'id': department.id,
                'name': department.name,
                'average_salary': str(department.average_salary),
            } for department in departments
        ]

    def post(self):
        """Create new department."""
        name = request.json['name']  # JS: POST {'name': 'IT'} /api/v1/departments
        department = Department(name=name)
        db.session.add(department)
        db.session.commit()
        result = {
            'id': department.id,
            'name': department.name,
        }
        return result, 201


class DepartmentResource(Resource):

    def get(self, department_id):
        """Get department by id."""
        department = self._get_department(department_id)
        employees = self._get_employees_by_id(department_id)
        department_obj = {
            'id': department.id,
            'name': department.name,
            'employees': [
                {
                    'id': employee.id,
                    'name': employee.name,
                    'salary': employee.salary,
                } for employee in employees
            ]
        }
        return department_obj, 200

    def put(self, department_id):
        """Update department parameter(s) by id."""
        department = self._get_department(department_id)
        department.name = request.json['name']
        db.session.commit()
        return {}, 200

    def delete(self, department_id):
        """Delete department by id."""
        department = self._get_department(department_id)
        db.session.delete(department)
        db.session.commit()
        return {}, 204

    def _get_department(self, department_id):
        return Department.query.get(department_id)

    def _get_employees_by_id(self, department_id):
        return Employee.query.filter_by(department_id=department_id)