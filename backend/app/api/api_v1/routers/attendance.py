#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db

from app.db.crud.post_graduations import edit_information, get_informations, create_attendance
from app.db import models as m

from app.schemas.base_schemas import AttendanceCreate, Attendance, AttendanceEdit
from app.core.auth import get_current_active_superuser, get_current_active_user

attendance_router = a = APIRouter()

@a.post("/contato", response_model=Attendance, response_model_exclude_none=True)
async def attendance_create(
    request: Request,
    attendance: AttendanceCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    """
    Create a new attendance
    """
    return create_attendance(db, attendance)

@a.put("/contato", response_model=Attendance, response_model_exclude_none=True)
async def attendance_edit(
        request: Request,
        attendance: AttendanceEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit attendance
    """
    attendance_id = get_informations(db, current_user.owner_id, m.Attendance)[0].id
    return edit_information(db, attendance_id, attendance, m.Attendance)
