"""initial migration

Revision ID: e95e9345b3fa
Revises:
Create Date: 2020-03-04 18:35:37.849182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e95e9345b3fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('name', sa.String),
        sa.Column('hashed_password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True)
    )
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('description', sa.String, index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("users.id"))
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('items')
