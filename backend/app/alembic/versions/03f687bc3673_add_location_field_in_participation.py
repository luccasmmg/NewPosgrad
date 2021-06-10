"""add location field in participation

Revision ID: 03f687bc3673
Revises: 52aecfaa3229
Create Date: 2021-06-10 03:13:55.146115-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f687bc3673'
down_revision = '52aecfaa3229'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('participation',
            sa.Column('location', sa.String(150)))

def downgrade():
    pass
