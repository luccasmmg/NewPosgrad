"""create participation table

Revision ID: 8ec02e840273
Revises: 9e894e16e8ee
Create Date: 2021-01-27 12:59:53.895967-08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec02e840273'
down_revision = '9e894e16e8ee'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "participation",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
            sa.Column("title", sa.String(150), nullable=False),
            sa.Column("description", sa.Text),
            sa.Column("year", sa.Integer),
            sa.Column("international", sa.Boolean),
            sa.Column("deleted", sa.Boolean, default=True))

def downgrade():
    op.drop_table("participation")
