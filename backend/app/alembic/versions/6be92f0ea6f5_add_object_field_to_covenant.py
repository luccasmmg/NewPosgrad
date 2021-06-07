"""add object field to covenant

Revision ID: 6be92f0ea6f5
Revises: e0365a260cb9
Create Date: 2021-06-07 06:18:42.294220-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6be92f0ea6f5'
down_revision = 'e0365a260cb9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('covenant',
            sa.Column('object', sa.Text))

def downgrade():
    pass
