"""add institutional repository field to course

Revision ID: aa3a827e7dee
Revises: 8e92450e1115
Create Date: 2021-02-26 16:42:22.216013-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa3a827e7dee'
down_revision = '8e92450e1115'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('course',
            sa.Column('institutional_repository_url', sa.String(150), nullable=False))

def downgrade():
    pass
