"""create oficial documents table

Revision ID: 02ac82781f22
Revises: 07cbd48521e3
Create Date: 2021-02-10 04:12:42.302436-08:00

"""
from alembic import op
import sqlalchemy as sa
import enum


# revision identifiers, used by Alembic.
revision = '02ac82781f22'
down_revision = '07cbd48521e3'
branch_labels = None
depends_on = None

class DocumentCategory(enum.Enum):
    records = 1
    regiments = 2
    resolutions = 3
    plans = 4
    others = 5

def upgrade():
    op.create_table(
        "official_document",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("owner_id", sa.Integer, sa.ForeignKey("post_graduation.id")),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("category", sa.Enum(DocumentCategory), nullable=False),
        sa.Column("cod", sa.String(15), nullable=False),
        sa.Column("file", sa.String(200), nullable=False),
        sa.Column("inserted_on", sa.DateTime(), server_default=sa.func.current_timestamp()),
        sa.Column("deleted", sa.Boolean, default=False),
    )

def downgrade():
    op.drop_table("official_document")
