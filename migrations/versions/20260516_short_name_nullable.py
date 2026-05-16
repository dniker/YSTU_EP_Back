"""Make discipline short_name nullable

Revision ID: 20260516_short_name_nullable
Revises: 20260516_add_is_actual
Create Date: 2026-05-16
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20260516_short_name_nullable'
down_revision: Union[str, None] = '20260516_add_is_actual'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'disciplines',
        'short_name',
        existing_type=sa.String(length=50),
        nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'disciplines',
        'short_name',
        existing_type=sa.String(length=50),
        nullable=False,
    )
