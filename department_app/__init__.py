from flask import Flask
from department_app.views import departments


def create_app():
    """Create and configure an instance of the Flask application."""
    from department_app.models.departments import db

    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.register_blueprint(departments.bp)
    db.init_app(app)

    return app
