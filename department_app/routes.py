from flask_restful import Api

from department_app.rest.v1.departments import DepartmentsResource, DepartmentResource
from department_app.rest.v1.employees import EmployeesResource, EmployeeResource
from department_app.views.departments import (
    index,
    department,
    employees,
    employee,
    employees_search,
)


def setup_routes(app):
    # Templates
    app.add_url_rule("/", "index", index, methods=["GET", "POST"])
    app.add_url_rule(
        "/department/<int:id>",
        "department",
        department,
        methods=["GET", "POST", "DELETE"],
    )
    app.add_url_rule("/employees", "employees", employees, methods=["GET", "POST"])
    app.add_url_rule(
        "/employees/search", "employees-search", employees_search, methods=["GET", "POST"]
    )
    app.add_url_rule("/employee/<int:id>", "employee", employee, methods=["GET", "POST"])

    # API
    api = Api(app)
    api.add_resource(DepartmentsResource, "/api/v1/departments")
    api.add_resource(DepartmentResource, "/api/v1/departments/<int:department_id>")
    api.add_resource(EmployeesResource, "/api/v1/employees")
    api.add_resource(EmployeeResource, "/api/v1/employees/<int:employee_id>")
