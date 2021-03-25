"""add status field to covenant

Revision ID: 19ccd5ff0188
Revises: aa3a827e7dee
Create Date: 2021-03-25 15:05:27.223412-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19ccd5ff0188'
down_revision = 'aa3a827e7dee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('covenant',
            sa.Column('finished', sa.Boolean, default=False))

def downgrade():
    pass
