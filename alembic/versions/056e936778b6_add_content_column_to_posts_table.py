"""add content column to posts table

Revision ID: 056e936778b6
Revises: ba09477fd733
Create Date: 2023-02-19 20:39:30.071811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056e936778b6'
down_revision = 'ba09477fd733'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
