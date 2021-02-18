"""add deleted to phones

Revision ID: b361cc407a5b
Revises: 9b913a4d0e9b
Create Date: 2021-02-18 10:14:47.800542-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b361cc407a5b'
down_revision = '9b913a4d0e9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('phone',
            sa.Column('deleted', sa.Boolean, default=False))

def downgrade():
    pass
