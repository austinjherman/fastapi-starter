"""create users table

Revision ID: ec9fcbc3f021
Revises:
Create Date: 2020-03-05 04:03:58.823117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec9fcbc3f021'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('password', sa.String)
    )


def downgrade():
    op.drop_table('users')
