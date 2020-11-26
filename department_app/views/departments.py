from flask import render_template, Blueprint

from department_app.models.departments import Department

bp = Blueprint("departments", __name__)


@bp.route("/", methods=["GET"])
def index():
    departments = Department.query.all()
    return render_template("departments.jinja2", departments=departments)
