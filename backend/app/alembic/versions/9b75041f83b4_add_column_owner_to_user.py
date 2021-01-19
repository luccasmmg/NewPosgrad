"""add column owner to user

Revision ID: 9b75041f83b4
Revises: 3b331f0968a8
Create Date: 2021-01-19 11:38:22.194033-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b75041f83b4'
down_revision = '3b331f0968a8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('owner_id', sa.Integer, sa.ForeignKey('post_graduation.id')))

def downgrade():
    op.drop_column('user', 'owner_id')
