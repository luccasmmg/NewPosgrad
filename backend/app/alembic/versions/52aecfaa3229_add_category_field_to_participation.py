"""add category field to participation

Revision ID: 52aecfaa3229
Revises: 77731d8baf60
Create Date: 2021-06-09 18:25:52.885643-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import enum


# revision identifiers, used by Alembic.
revision = '52aecfaa3229'
down_revision = '77731d8baf60'
branch_labels = None
depends_on = None

class ParticipationCategory(enum.Enum):
    cooperation_agreement = 1
    prizes = 2
    parternships = 3
    events = 4
    posdocs = 5


def upgrade():
    participation_category = postgresql.ENUM('cooperation_agreement', 'prize', 'event', 'parternship', 'posdoc', name='parternship_category')
    participation_category.create(op.get_bind())
    
    op.add_column('participation',
            sa.Column('category', sa.Enum('cooperation_agreement', 'prize', 'event', 'parternship', 'posdoc', name='parternship_category'), nullable=False)) 

def downgrade():
    pass
