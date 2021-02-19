"""add events

Revision ID: 399fd384916b
Revises: 77c1ede3a115
Create Date: 2021-02-19 08:10:02.721477-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '399fd384916b'
down_revision = '77c1ede3a115'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "event",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("link", sa.String(200)),
        sa.Column("initial_date", sa.DateTime()),
        sa.Column("final_date", sa.DateTime()),
        sa.Column("deleted", sa.Boolean, default=False),
    )


def downgrade():
    op.drop_table("event")
