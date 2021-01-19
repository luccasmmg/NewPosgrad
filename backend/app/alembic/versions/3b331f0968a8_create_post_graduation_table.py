"""create post_graduation table

Revision ID: 3b331f0968a8
Revises: 91979b40eb38
Create Date: 2021-01-19 11:33:41.998665-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b331f0968a8'
down_revision = '91979b40eb38'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "post_graduation",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("id_unit", sa.Integer, unique=True, nullable=False),
        sa.Column("name", sa.String(50), unique=True, nullable=False),
        sa.Column("initials", sa.String(10), unique=True, nullable=False),
        sa.Column("sigaa_code", sa.Integer, unique=True, nullable=False),
        sa.Column("is_signed_in", sa.Boolean, default=True),
        sa.Column("old_url", sa.String, default=""),
        sa.Column("description_small", sa.Text, default=""),
        sa.Column("description_big", sa.Text, default=""),
    )
def downgrade():
    op.drop_table("post_graduation")
