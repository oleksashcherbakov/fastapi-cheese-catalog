"""Initial migration

Revision ID: 69fe108d1729
Revises: 0e439c3b7585
Create Date: 2025-08-27 15:52:39.023317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69fe108d1729'
down_revision: Union[str, Sequence[str], None] = '0e439c3b7585'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Используем batch_alter_table для поддержки SQLite
    with op.batch_alter_table('cheese') as batch_op:
        batch_op.create_foreign_key(
            'fk_cheese_cheese_type',
            'cheese_type',
            ['cheese_type_id'],
            ['id']
        )


def downgrade() -> None:
    with op.batch_alter_table('cheese') as batch_op:
        batch_op.drop_constraint('fk_cheese_cheese_type', type_='foreignkey')
    op.drop_column('cheese', 'cheese_type_id')
    # ### end Alembic commands ###
