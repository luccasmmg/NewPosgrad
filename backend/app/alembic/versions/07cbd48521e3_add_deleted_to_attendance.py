"""add deleted to attendance

Revision ID: 07cbd48521e3
Revises: ac434aa815c4
Create Date: 2021-01-28 11:26:50.957920-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07cbd48521e3'
down_revision = 'ac434aa815c4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('attendance',
            sa.Column('deleted', sa.Boolean, default=False))

def downgrade():
    pass
