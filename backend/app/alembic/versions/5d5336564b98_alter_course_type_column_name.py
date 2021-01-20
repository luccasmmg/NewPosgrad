"""alter course type column name

Revision ID: 5d5336564b98
Revises: 66f906f7fb48
Create Date: 2021-01-20 07:07:21.253167-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5336564b98'
down_revision = '66f906f7fb48'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "course",
        "type",
        new_column_name="course_type"
    )

def downgrade():
    pass
