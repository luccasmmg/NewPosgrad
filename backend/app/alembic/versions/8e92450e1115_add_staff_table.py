"""add staff table

Revision ID: 8e92450e1115
Revises: 9893b0de12f2
Create Date: 2021-02-22 12:48:37.194126-08:00

"""
from alembic import op
import sqlalchemy as sa
import enum


# revision identifiers, used by Alembic.
revision = '8e92450e1115'
down_revision = '9893b0de12f2'
branch_labels = None
depends_on = None

class Rank(enum.Enum):
    coordinator = 1
    vice_coordinator = 2
    secretariat = 3
    intern = 4

def upgrade():
    op.create_table(
        "staff",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("rank", sa.Enum(Rank), nullable=False),
        sa.Column("description", sa.Text),
        sa.Column("photo", sa.String(200)),
        sa.Column("deleted", sa.Boolean, default=False),
    )

def downgrade():
    op.drop_table("staff")
