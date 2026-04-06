from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import StudentCreate, StudentResponse, StudentList, StudentUpdate
from ..services.student_service import (
    create_student,
    get_student,
    update_student,
    soft_delete_student,
    list_students,
)
from uuid import UUID

router = APIRouter()


@router.post("/", response_model=StudentResponse, status_code=201)
async def create(payload: StudentCreate, db: AsyncSession = Depends(get_db)):
    obj = await create_student(db, payload)
    return obj


@router.get("/", response_model=StudentList)
async def list_all(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    course: str | None = None,
    grade: str | None = None,
    is_active: bool | None = None,
    min_gpa: float | None = None,
    max_gpa: float | None = None,
    db: AsyncSession = Depends(get_db),
):
    total, items = await list_students(db, page, limit, course, grade, is_active, min_gpa, max_gpa)
    return {"total": total, "page": page, "limit": limit, "data": items}


@router.get("/{student_id}", response_model=StudentResponse)
async def get_one(student_id: UUID, db: AsyncSession = Depends(get_db)):
    obj = await get_student(db, student_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    return obj


@router.patch("/{student_id}", response_model=StudentResponse)
async def patch(student_id: UUID, payload: StudentUpdate, db: AsyncSession = Depends(get_db)):
    obj = await update_student(db, student_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    return obj


@router.delete("/{student_id}")
async def delete(student_id: UUID, db: AsyncSession = Depends(get_db)):
    obj = await soft_delete_student(db, student_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "deleted"}
