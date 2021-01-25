from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.courses import (
    get_course,
    create_course,
    edit_course,
    delete_course,
)
from app.schemas.base_schemas import CourseCreate, Course, CourseEdit
from app.core.auth import get_current_active_superuser, get_current_active_user

course_router = c = APIRouter()

@c.post("/curso", response_model=Course, response_model_exclude_none=True)
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

@c.delete("/curso/{course_id}", response_model=Course, response_model_exclude_none=True)
async def course_delete(
        request: Request,
        course_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete course
    """
    return delete_course(db, get_course(db, course_id).id)

@c.put("/curso/{course_id}", response_model=Course, response_model_exclude_none=True)
async def course_edit(
        request: Request,
        course_id: int,
        course: CourseEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit course
    """
    return edit_course(db, get_course(db, course_id).id, course)
