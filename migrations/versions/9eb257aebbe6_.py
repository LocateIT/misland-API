"""Intial database

Revision ID: 9eb257aebbe6
Revises: 
Create Date: 2017-04-05 13:39:32.398761

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from misland_api.models import GUID

# revision identifiers, used by Alembic.
revision = '9eb257aebbe6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', GUID(), autoincrement=False, nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('script',
    sa.Column('id', GUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('slug', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', GUID(), nullable=True),
    sa.Column('status', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('execution',
    sa.Column('id', GUID(), autoincrement=False, nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.Column('params', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('results', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('script_id', GUID(), nullable=True),
    sa.ForeignKeyConstraint(['script_id'], ['script.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('script_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('script_id', GUID(), nullable=True),
    sa.ForeignKeyConstraint(['script_id'], ['script.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('execution_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('level', sa.String(length=80), nullable=False),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.Column('execution_id', GUID(), nullable=True),
    sa.ForeignKeyConstraint(['execution_id'], ['execution.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('execution_log')
    op.drop_table('script_log')
    op.drop_table('execution')
    op.drop_table('script')
    op.drop_table('user')
    # ### end Alembic commands ###
