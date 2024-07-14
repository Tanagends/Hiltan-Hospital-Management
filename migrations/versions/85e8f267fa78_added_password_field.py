"""added password field

Revision ID: 85e8f267fa78
Revises: 5ac8b5ff8afc
Create Date: 2024-07-15 00:14:32.251185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85e8f267fa78'
down_revision = '5ac8b5ff8afc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=50), nullable=True))

    with op.batch_alter_table('nurses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=50), nullable=True))

    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_column('password')

    with op.batch_alter_table('nurses', schema=None) as batch_op:
        batch_op.drop_column('password')

    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###