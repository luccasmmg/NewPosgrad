"""add institutional repository field to course

Revision ID: e0365a260cb9
Revises: 19ccd5ff0188
Create Date: 2021-06-06 17:07:22.674673-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0365a260cb9'
down_revision = '19ccd5ff0188'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "repository",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("author", sa.String(100)),
        sa.Column("title", sa.String(500)),
        sa.Column("year", sa.Integer),
        sa.Column("link", sa.String(200)),
        sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("repository")
