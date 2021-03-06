"""Remove recipieints col from emails table

Revision ID: e5334c30fd32
Revises: 85fe3e197a58
Create Date: 2022-06-27 22:44:37.254117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5334c30fd32'
down_revision = '85fe3e197a58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('emails', 'recipients')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('emails', sa.Column('recipients', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
