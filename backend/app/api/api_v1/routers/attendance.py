#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db

from app.db.crud.post_graduations import get_post_graduation, edit_information, get_informations, delete_information, get_information, create_attendance, create_phone
from app.db import models as m

from app.schemas.base_schemas import AttendanceCreate, Attendance, AttendanceEdit, Phone, PhoneCreate, PhoneEdit
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

@a.post("/contato/telefone", response_model=Phone, response_model_exclude_none=True)
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
    attendance_id = get_informations(db, current_user.owner_id, m.Attendance).first()
    return edit_information(db, attendance_id, attendance, m.Attendance)

@a.delete("/contato/telefone/{phone_id}", response_model=Phone, response_model_exclude_none=True)
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

@a.put("/contato/telefone/{phone_id}", response_model=Phone, response_model_exclude_none=True)
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
