from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..services.student_service import get_student
from ..services.ai_service import call_openai_summary
from uuid import UUID

router = APIRouter()


@router.get("/{student_id}/summary")
async def summary(student_id: UUID, db: AsyncSession = Depends(get_db)):
    student = await get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    try:
        payload = {k: getattr(student, k) for k in [
            "first_name", "last_name", "email", "phone", "course", "grade", "gpa", "enrolled_at"
        ]}
        summary_text = call_openai_summary(payload)
        return {"summary": summary_text}
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception:
        raise HTTPException(status_code=503, detail="AI service currently unavailable")
