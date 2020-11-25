from flask import Flask

from department_app.views import departments


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.register_blueprint(departments.bp)
    return app
