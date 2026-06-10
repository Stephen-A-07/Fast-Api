"""create post table

Revision ID: 136e5dc11a51
Revises: 
Create Date: 2026-06-10 18:09:46.930083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '136e5dc11a51'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
