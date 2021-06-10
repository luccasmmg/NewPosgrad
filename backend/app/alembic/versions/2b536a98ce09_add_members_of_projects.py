"""add members of projects

Revision ID: 2b536a98ce09
Revises: 4c6d43e70e5a
Create Date: 2021-06-10 05:33:54.660468-07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b536a98ce09'
down_revision = '4c6d43e70e5a'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
            "project_member",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("project", sa.Integer, sa.ForeignKey("project.id")),
            sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
            sa.Column("name", sa.String(300), nullable=False),
            sa.Column("job_title", sa.String(300)),
            sa.Column("deleted", sa.Boolean, default=False)
    )

def downgrade():
    op.drop_table("project_member")
