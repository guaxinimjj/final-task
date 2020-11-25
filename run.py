"""Entry point for gunicorn runner."""
from department_app import create_app
from dotenv import load_dotenv

load_dotenv()
app = create_app()
