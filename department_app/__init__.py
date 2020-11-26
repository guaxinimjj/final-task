from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from department_app.views import departments

db = SQLAlchemy()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(departments.bp)
    db.init_app(app)

    return app
