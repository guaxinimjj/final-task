from department_app.models import db


class Department(db.Model):
    """Create Department table"""

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Department %r>" % self.id


class Employee(db.Model):
    """Create Employee table"""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    date_birth = db.Column(db.Date, nullable=False)
    salary = db.Column(db.DECIMAL, nullable=False)

    def __repr__(self):
        return "<Employee %r>" % self.id
