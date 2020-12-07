from flask import Flask
from department_app.views import departments
from department_app.routes import setup_routes


def create_app():
    """Create and configure an instance of the Flask application."""
    from department_app.models import db

    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    setup_routes(app)
    db.init_app(app)

    return app
