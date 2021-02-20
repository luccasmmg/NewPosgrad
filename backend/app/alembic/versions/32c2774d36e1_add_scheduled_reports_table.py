"""add scheduled reports table

Revision ID: 32c2774d36e1
Revises: 399fd384916b
Create Date: 2021-02-20 07:24:03.633179-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32c2774d36e1'
down_revision = '399fd384916b'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        "scheduled_report",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("author", sa.String(150), nullable=False),
        sa.Column("datetime", sa.DateTime(), nullable=False),
        sa.Column("location", sa.String(150)),
        sa.Column("deleted", sa.Boolean, default=False),
    )

def downgrade():
    op.drop_table("scheduled_report")
