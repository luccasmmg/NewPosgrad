from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.courses import (
    get_course,
    create_course,
)
from app.schemas.base_schemas import CourseCreate, Course
from app.core.auth import get_current_active_superuser

course_router = c = APIRouter()

@c.post("/course", response_model=Course, response_model_exclude_none=True)
async def course_create(
    request: Request,
    course: CourseCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Create a new course
    """
    return create_course(db, course)
