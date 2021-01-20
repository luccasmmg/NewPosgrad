"""create course tables

Revision ID: 66f906f7fb48
Revises: 9b75041f83b4
Create Date: 2021-01-20 02:39:20.442308-08:00

"""
from alembic import op
import enum
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66f906f7fb48'
down_revision = '9b75041f83b4'
branch_labels = None
depends_on = None

class CourseType(enum.Enum):
    masters = 1
    doctorate = 2

def upgrade():
    op.create_table(
        "course",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("id_sigaa", sa.Integer, nullable=False),
        sa.Column("type", sa.Enum(CourseType), nullable=False),
    )


def downgrade():
    op.drop_table("course")
