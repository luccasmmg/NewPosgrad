"""add phones

Revision ID: 9b913a4d0e9b
Revises: 02ac82781f22
Create Date: 2021-02-18 10:01:13.697755-08:00

"""
from alembic import op
import sqlalchemy as sa

import enum

# revision identifiers, used by Alembic.
revision = '9b913a4d0e9b'
down_revision = '02ac82781f22'
branch_labels = None
depends_on = None

class PhoneType(enum.Enum):
    fixed = 1
    cellphone = 2

def upgrade():
    op.create_table(
            "phone",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("owner_attendance_id", sa.Integer, sa.ForeignKey("attendance.id")),
            sa.Column("number", sa.Integer, nullable=False),
            sa.Column("phone_type", sa.Enum(PhoneType), nullable=False),
    )

def downgrade():
    op.drop_table("phone")
