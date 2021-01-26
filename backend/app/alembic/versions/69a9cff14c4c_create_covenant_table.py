"""create covenant table

Revision ID: 69a9cff14c4c
Revises: 0ef989ab3bb8
Create Date: 2021-01-26 11:56:16.871842-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69a9cff14c4c'
down_revision = '0ef989ab3bb8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "covenant",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("logo_file", sa.String(200)),
        sa.Column("initials", sa.String(10)),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("covenant")
