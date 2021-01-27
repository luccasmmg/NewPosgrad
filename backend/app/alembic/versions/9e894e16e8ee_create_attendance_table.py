"""create attendance table

Revision ID: 9e894e16e8ee
Revises: 69a9cff14c4c
Create Date: 2021-01-26 16:17:24.484885-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e894e16e8ee'
down_revision = '69a9cff14c4c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "attendance",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
            sa.Column("location", sa.String(150), default=""),
            sa.Column("email", sa.String(150), default=""),
            sa.Column("schedule", sa.String(150), default=""),
    )

def downgrade():
    op.drop_table("attendance")
