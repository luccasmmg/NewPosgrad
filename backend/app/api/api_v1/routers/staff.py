#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3
from os.path import splitext

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_staff
from app.db import models as m

from app.schemas.pg_information_schemas import StaffCreate, Staff, StaffEdit
from app.core.auth import get_current_active_user

staff_router = s = APIRouter()

@s.post("/equipe", response_model=Staff, response_model_exclude_none=True)
async def covenant_create(
    request: Request,
    db=Depends(get_db),
    name: str = Form(...),
    description: str = Form(...),
    rank: str = Form(...),
    photo: UploadFile = File(...),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new staff member
    """
    if not photo.filename.endswith(('.jpg', '.jpeg', '.png')):
        raise HTTPException(status_code=422, detail="The photo file has to be in .jpg .jpeg or .png")

    filename_normalized = "".join(x for x in splitext(photo.filename)[0] if x.isalnum()) + splitext(photo.filename)[1]

    s3_response = boto3.resource('s3').Bucket('juno-minerva').put_object(Key=f'staff_photos/{filename_normalized}', Body=photo.file, ACL='public-read')

    staff = StaffCreate(name=name, description=description, rank=rank, photo=f'https://juno-minerva.s3-sa-east-1.amazonaws.com/staff_photos/{filename_normalized}')

    return create_staff(db, current_user.owner_id, staff)

@s.delete("/equipe/{staff_id}", response_model=Staff, response_model_exclude_none=True)
async def staff_delete(
        request: Request,
        staff_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete staff
    """
    return delete_information(db, get_information(db, staff_id, m.Staff).id, m.Staff)

@s.put("/equipe/{staff_id}", response_model=Staff, response_model_exclude_none=True)
async def staff_edit(
        request: Request,
        staff_id: int,
        staff: StaffEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit staff
    """
    return edit_information(db, get_information(db, staff_id, m.Staff).id, staff, m.Staff)
