"""create students table

Revision ID: 0001_create_students
Revises: 
Create Date: 2026-04-06 00:00:00.000000
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0001_create_students'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # create extension if not exists
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    op.create_table(
        'students',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('first_name', sa.String(length=100), nullable=False),
        sa.Column('last_name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('course', sa.String(length=150), nullable=False),
        sa.Column('grade', sa.String(length=5), nullable=True),
        sa.Column('gpa', sa.Float(), nullable=True),
        sa.Column('enrolled_at', sa.Date(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_index(op.f('ix_students_email'), 'students', ['email'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_students_email'), table_name='students')
    op.drop_table('students')
