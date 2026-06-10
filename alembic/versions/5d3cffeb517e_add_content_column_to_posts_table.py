"""add content column to posts table

Revision ID: 5d3cffeb517e
Revises: 136e5dc11a51
Create Date: 2026-06-10 18:19:19.267656

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '5d3cffeb517e'
down_revision: Union[str, Sequence[str], None] = '136e5dc11a51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
