#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_student_advisor
from app.db import models as m

from app.schemas.pg_information_schemas import StudentAdvisorCreate, StudentAdvisor, StudentAdvisorEdit
from app.core.auth import get_current_active_user

student_advisor_router = c = APIRouter()

@c.post("/coordenador", response_model=StudentAdvisor, response_model_exclude_none=True)
async def student_advisor_create(
    request: Request,
    student_advisor: StudentAdvisorCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new advisors
    """
    return create_student_advisor(db, current_user.owner_id, student_advisor)

@c.delete("/coordenador/{student_advisor_id}", response_model=StudentAdvisor, response_model_exclude_none=True)
async def student_advisor_delete(
        request: Request,
        student_advisor_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete advisor
    """
    return delete_information(db, get_information(db, student_advisor_id, m.StudentAdvisor).id, m.StudentAdvisor)

@c.put("/coordenador/{student_advisor_id}", response_model=StudentAdvisor, response_model_exclude_none=True)
async def student_advisor_edit(
        request: Request,
        student_advisor_id: int,
        student_advisor: StudentAdvisorEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit advisor
    """
    return edit_information(db, get_information(db, student_advisor_id, m.StudentAdvisor).id, student_advisor, m.StudentAdvisor)
