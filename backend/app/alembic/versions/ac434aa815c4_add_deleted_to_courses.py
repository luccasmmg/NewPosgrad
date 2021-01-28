"""add deleted to courses

Revision ID: ac434aa815c4
Revises: 8ec02e840273
Create Date: 2021-01-28 11:01:12.522085-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac434aa815c4'
down_revision = '8ec02e840273'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('course',
            sa.Column('deleted', sa.Boolean, default=False))

def downgrade():
    pass
