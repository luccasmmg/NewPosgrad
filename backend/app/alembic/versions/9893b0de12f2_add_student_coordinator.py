"""add student coordinator

Revision ID: 9893b0de12f2
Revises: 32c2774d36e1
Create Date: 2021-02-22 05:16:17.947827-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9893b0de12f2'
down_revision = '32c2774d36e1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "student_advisor",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("registration", sa.String(50), nullable=False),
        sa.Column("advisor_name", sa.String(150), nullable=False),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("student_advisor")
