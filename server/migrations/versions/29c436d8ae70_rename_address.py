"""rename address

Revision ID: 29c436d8ae70
Revises: 511a5d0853a4
Create Date: 2024-01-07 17:12:51.618169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c436d8ae70'
down_revision = '511a5d0853a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###