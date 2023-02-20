"""add foreign-key to posts table

Revision ID: 09415518ad34
Revises: 9306ba937b70
Create Date: 2023-02-19 21:00:45.630098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09415518ad34'
down_revision = '9306ba937b70'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", 
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
