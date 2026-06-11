"""add last few columns to posts table

Revision ID: cc4e4d1188f5
Revises: 66b0311350ef
Create Date: 2026-06-11 15:16:15.762435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc4e4d1188f5'
down_revision: Union[str, Sequence[str], None] = '66b0311350ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable = False,server_default= 'TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default= sa.text('NOW()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
