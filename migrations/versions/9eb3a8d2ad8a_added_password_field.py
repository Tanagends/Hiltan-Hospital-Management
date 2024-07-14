"""added password field

Revision ID: 9eb3a8d2ad8a
Revises: 1d01535e87e0
Create Date: 2024-07-15 00:19:50.889990

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9eb3a8d2ad8a'
down_revision = '1d01535e87e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=200),
               existing_nullable=True)

    with op.batch_alter_table('nurses', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=200),
               existing_nullable=True)

    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=200),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    with op.batch_alter_table('nurses', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    with op.batch_alter_table('doctors', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###