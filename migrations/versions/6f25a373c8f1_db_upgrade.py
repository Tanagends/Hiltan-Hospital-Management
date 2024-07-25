"""db upgrade

Revision ID: 6f25a373c8f1
Revises: 7d563a0d7e34
Create Date: 2024-07-25 21:17:07.377131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f25a373c8f1'
down_revision = '7d563a0d7e34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doctor_id', sa.String(length=50), nullable=True))
        batch_op.create_foreign_key(None, 'doctors', ['doctor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('diagnosis', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('doctor_id')

    # ### end Alembic commands ###
