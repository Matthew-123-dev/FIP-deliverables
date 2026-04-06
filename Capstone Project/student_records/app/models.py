import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = sa.Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()'))
    first_name = sa.Column(sa.String(100), nullable=False)
    last_name = sa.Column(sa.String(100), nullable=False)
    email = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    phone = sa.Column(sa.String(20), nullable=True)
    course = sa.Column(sa.String(150), nullable=False)
    grade = sa.Column(sa.String(5), nullable=True)
    gpa = sa.Column(sa.Float, nullable=True)
    enrolled_at = sa.Column(sa.Date, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False, server_default=sa.text('true'))
    created_at = sa.Column(sa.DateTime, server_default=func.now(), nullable=False)
    updated_at = sa.Column(sa.DateTime, onupdate=func.now(), nullable=True)
