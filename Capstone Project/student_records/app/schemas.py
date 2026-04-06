from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date, datetime
from uuid import UUID


class StudentCreate(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    email: EmailStr
    phone: Optional[str] = None
    course: str = Field(..., max_length=150)
    grade: Optional[str] = Field(None, max_length=5)
    gpa: Optional[float] = None
    enrolled_at: date


class StudentUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    course: Optional[str] = Field(None, max_length=150)
    grade: Optional[str] = Field(None, max_length=5)
    gpa: Optional[float] = None
    enrolled_at: Optional[date] = None
    is_active: Optional[bool] = None


class StudentResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    course: str
    grade: Optional[str]
    gpa: Optional[float]
    enrolled_at: date
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class StudentList(BaseModel):
    total: int
    page: int
    limit: int
    data: List[StudentResponse]


class SearchParams(BaseModel):
    q: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[str] = None
    is_active: Optional[bool] = None
    min_gpa: Optional[float] = None
    max_gpa: Optional[float] = None
