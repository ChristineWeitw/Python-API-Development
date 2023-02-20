"""add last few columns to posts table

Revision ID: 6fc9ef99e4f0
Revises: 09415518ad34
Create Date: 2023-02-19 21:05:27.212589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc9ef99e4f0'
down_revision = '09415518ad34'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
                sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
