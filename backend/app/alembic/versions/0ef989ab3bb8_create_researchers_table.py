"""create researchers table

Revision ID: 0ef989ab3bb8
Revises: 5d5336564b98
Create Date: 2021-01-25 08:40:08.796626-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ef989ab3bb8'
down_revision = '5d5336564b98'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "researcher",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("cpf", sa.String(11), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("researcher")
