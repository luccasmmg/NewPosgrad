"""add news

Revision ID: 77c1ede3a115
Revises: b361cc407a5b
Create Date: 2021-02-19 06:12:59.911428-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77c1ede3a115'
down_revision = 'b361cc407a5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "news",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("headline", sa.String(150)),
        sa.Column("body", sa.Text),
        sa.Column("date", sa.Date),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    pass
