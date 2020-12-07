from setuptools import setup, find_packages


setup(
    name="Department app",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "alembic==1.4.3",
        "flask==1.1.2",
        "flask-sqlalchemy==2.4.4",
        "flask-restful==0.3.8",
        "gunicorn==20.0.4",
        "psycopg2==2.8.6",
        "python-dotenv==0.15.0",
    ],
    extras_require={
        "ci": [
            "black==20.8b1",
            "coveralls==2.2.0",
            "pylint==2.6.0",
            "pylint_flask==0.6",
            "pylint_flask_sqlalchemy==0.2.0",
            "pytest==6.1.2",
            "pytest-cov==2.10.1",
        ]
    },
)
