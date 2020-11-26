"""insert-data

Revision ID: c3683febfcf8
Revises: ffbf391d4338
Create Date: 2020-11-26 12:23:29.194054

"""
import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c3683febfcf8"
down_revision = "ffbf391d4338"
branch_labels = None
depends_on = None


def upgrade():
    # get metadata from current connection
    meta = sa.MetaData(bind=op.get_bind())

    # pass in tuple with tables we want to reflect, otherwise whole database will get reflected
    meta.reflect(only=("departments", "employees"))

    # define table representation
    departments = sa.Table("departments", meta)
    employees = sa.Table("employees", meta)
    # insert records
    op.bulk_insert(
        departments,
        [
            {"name": "IT"},
            {"name": "Security"},
        ],
    )

    op.bulk_insert(
        employees,
        [
            {
                "name": "Bob Rob",
                "department_id": 1,
                "date_birth": datetime.date(1993, 8, 24),
                "salary": 5000,
            },
            {
                "name": "Tod Cob",
                "department_id": 1,
                "date_birth": datetime.date(1996, 9, 4),
                "salary": 3000,
            },
            {
                "name": "Spay",
                "department_id": 2,
                "date_birth": datetime.date(1991, 5, 14),
                "salary": 7000,
            },
        ],
    )


def downgrade():
    pass
