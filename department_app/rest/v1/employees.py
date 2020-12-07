from flask import request
from flask_restful import Resource

from department_app.models import db
from department_app.models.departments import Employee
from department_app.models.utils import (
    get_department_by_id,
    get_employee_query,
    get_employee_by_id,
    get_search_query,
)


class EmployeesResource(Resource):
    """Resource for employees."""

    def get(self):
        """Get employees."""
        where = get_search_query(request.args)
        query = get_employee_query(where)
        employees = query.all()
        return [
            {
                "id": employee.id,
                "name": employee.name,
                "salary": str(employee.salary),
                "date_birth": employee.date_birth.isoformat(),
                "department_name": employee.department_name,
            }
            for employee in employees
        ], 200

    def post(self):
        """Create new employee."""
        name = request.json["name"]
        date = request.json["date"]
        salary = request.json["salary"]
        department_id = request.json["depart_name"]

        employee = Employee(
            name=name, department_id=department_id, date_birth=date, salary=salary
        )
        db.session.add(employee)
        db.session.commit()

        department = get_department_by_id(department_id)

        result = {
            "id": employee.id,
            "name": employee.name,
            "salary": str(employee.salary),
            "date_birth": employee.date_birth,
            "department_name": department.name,
        }
        return result, 201


class EmployeeResource(Resource):
    """Resource for employee."""

    def get(self, employee_id):
        """Get employee by id.."""
        employee = get_employee_by_id(employee_id)
        result = {
            "id": employee.id,
            "name": employee.name,
            "salary": str(employee.salary),
            "date_birth": employee.date_birth,
            "department_name": employee.department_name,
        }
        return result

    def put(self, employee_id):
        """Update employee parameter(s) by id."""
        # request.json
        employee = get_employee_by_id(employee_id)
        employee.todo
        return {}, 200

    def delete(self, employee_id):
        """Delete employee by id."""
        employee = Employee.query.get(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return {}, 204
