from sqlalchemy import select, func, and_, or_, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple
from ..models import Student
from ..schemas import StudentCreate, StudentUpdate
from uuid import UUID


async def create_student(db: AsyncSession, payload: StudentCreate) -> Student:
    obj = Student(**payload.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_student(db: AsyncSession, student_id: UUID) -> Student | None:
    q = select(Student).where(Student.id == student_id)
    result = await db.execute(q)
    return result.scalars().first()


async def update_student(db: AsyncSession, student_id: UUID, payload: StudentUpdate) -> Student | None:
    obj = await get_student(db, student_id)
    if not obj:
        return None
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def soft_delete_student(db: AsyncSession, student_id: UUID) -> Student | None:
    obj = await get_student(db, student_id)
    if not obj:
        return None
    obj.is_active = False
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def list_students(
    db: AsyncSession,
    page: int = 1,
    limit: int = 20,
    course: str | None = None,
    grade: str | None = None,
    is_active: bool | None = None,
    min_gpa: float | None = None,
    max_gpa: float | None = None,
) -> Tuple[int, List[Student]]:
    q = select(Student)
    filters = []
    if course:
        filters.append(Student.course == course)
    if grade:
        filters.append(Student.grade == grade)
    if is_active is not None:
        filters.append(Student.is_active == is_active)
    if min_gpa is not None:
        filters.append(Student.gpa >= min_gpa)
    if max_gpa is not None:
        filters.append(Student.gpa <= max_gpa)
    if filters:
        q = q.where(and_(*filters))

    count_q = select(func.count()).select_from(Student)
    if filters:
        count_q = count_q.where(and_(*filters))

    total = (await db.execute(count_q)).scalar_one()

    q = q.offset((page - 1) * limit).limit(limit)
    result = await db.execute(q)
    items = result.scalars().all()
    return total, items


async def search_students(
    db: AsyncSession,
    qstr: str | None,
    page: int = 1,
    limit: int = 20,
    course: str | None = None,
    grade: str | None = None,
    is_active: bool | None = None,
) -> Tuple[int, List[Student]]:
    q = select(Student)
    filters = []
    if qstr:
        like = f"%{qstr}%"
        filters.append(or_(
            Student.first_name.ilike(like),
            Student.last_name.ilike(like),
            Student.email.ilike(like),
            Student.course.ilike(like),
        ))
    if course:
        filters.append(Student.course == course)
    if grade:
        filters.append(Student.grade == grade)
    if is_active is not None:
        filters.append(Student.is_active == is_active)

    if filters:
        q = q.where(and_(*filters))

    count_q = select(func.count()).select_from(Student)
    if filters:
        count_q = count_q.where(and_(*filters))

    total = (await db.execute(count_q)).scalar_one()

    q = q.offset((page - 1) * limit).limit(limit)
    result = await db.execute(q)
    items = result.scalars().all()
    return total, items
