"""add impact

Revision ID: 17a8cdb86822
Revises: 6be92f0ea6f5
Create Date: 2021-06-08 06:01:32.004751-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17a8cdb86822'
down_revision = '6be92f0ea6f5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "impact",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("body", sa.Text),
        sa.Column("inserted_on", sa.Date),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("impact")
