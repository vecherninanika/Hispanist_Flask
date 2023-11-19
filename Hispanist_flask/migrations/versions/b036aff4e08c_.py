"""empty message

Revision ID: b036aff4e08c
Revises: dc38d2d4c979
Create Date: 2023-11-18 13:17:39.905791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b036aff4e08c'
down_revision: Union[str, None] = 'dc38d2d4c979'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videos', sa.Column('description', sa.String(), nullable=True))
    op.alter_column('videos', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('videos', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('videos', 'description')
    # ### end Alembic commands ###