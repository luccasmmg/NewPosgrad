"""add projects

Revision ID: 4c6d43e70e5a
Revises: 03f687bc3673
Create Date: 2021-06-10 03:37:07.341548-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c6d43e70e5a'
down_revision = '03f687bc3673'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "project",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
            sa.Column("coordinator", sa.Integer, sa.ForeignKey("researcher.id")),
            sa.Column("name", sa.String(300), nullable=False),
            sa.Column("status", sa.String(150), default=""),
            sa.Column("email", sa.String(150), default=""),
            sa.Column("year", sa.Integer),
            sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("project")
