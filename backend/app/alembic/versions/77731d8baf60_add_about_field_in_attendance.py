"""add about field in attendance

Revision ID: 77731d8baf60
Revises: 17a8cdb86822
Create Date: 2021-06-09 02:45:53.323147-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77731d8baf60'
down_revision = '17a8cdb86822'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('attendance',
            sa.Column('about', sa.Text))

def downgrade():
    pass
