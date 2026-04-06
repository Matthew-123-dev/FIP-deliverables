from fastapi import APIRouter, Depends, Query
from ..database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from ..services.student_service import search_students
from ..schemas import StudentList

router = APIRouter()


@router.get("/", response_model=StudentList)
async def search(
    q: str | None = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    course: str | None = None,
    grade: str | None = None,
    is_active: bool | None = None,
    db: AsyncSession = Depends(get_db),
):
    total, items = await search_students(db, q, page, limit, course, grade, is_active)
    return {"total": total, "page": page, "limit": limit, "data": items}
