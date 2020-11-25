from flask import render_template, Blueprint

bp = Blueprint("departments", __name__)


@bp.route("/", methods=["GET"])
def index():
    return render_template("departments.jinja2")
