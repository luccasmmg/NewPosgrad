#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db

from app.db.crud.post_graduations import get_post_graduation, edit_information, get_informations, delete_information, get_information, create_attendance, create_phone
from app.db import models as m

from app.schemas.base_schemas import AttendanceCreate, Attendance, AttendanceEdit, Phone, PhoneCreate, PhoneEdit
from app.core.auth import get_current_active_superuser, get_current_active_user

attendance_router = a = APIRouter()

@a.get("/contato", response_model=t.List[Attendance], response_model_exclude_none=True)
async def get_attendances(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    attendances = get_informations(db, current_user.owner_id, m.Attendance).all()
    response.headers["Content-Range"] = f"0-9/{len(attendances)}"
    return attendances

@a.get("/contato/{attendance_id}", response_model=Attendance, response_model_exclude_none=True)
async def attendance_details(
        response: Response,
        attendance_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, attendance_id, m.Attendance)

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


@a.put("/contato/{attendance_id}", response_model=Attendance, response_model_exclude_none=True)
async def attendance_edit(
        request: Request,
        attendance_id: int,
        attendance: AttendanceEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit attendance
    """
    return edit_information(db, attendance_id, attendance, m.Attendance)

@a.post("/telefone", response_model=Phone, response_model_exclude_none=True)
async def phone_create(
    request: Request,
    phone: PhoneCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new phone
    """
    attendance_id = get_post_graduation(db, current_user.owner_id).attendance.id
    return create_phone(db, attendance_id, phone)

@a.delete("/telefone/{phone_id}", response_model=Phone, response_model_exclude_none=True)
async def phone_delete(
        request: Request,
        phone_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete phone
    """
    return delete_information(db, get_information(db, phone_id, m.Phone).id, m.Phone)

@a.put("/telefone/{phone_id}", response_model=Phone, response_model_exclude_none=True)
async def phone_edit(
        request: Request,
        phone_id: int,
        phone: PhoneEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit phone
    """
    return edit_information(db, get_information(db, phone_id, m.Phone).id, phone, m.Phone)
