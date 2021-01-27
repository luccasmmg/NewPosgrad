#!/usr/bin/env python3
#
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import base_schemas

def get_attendance(db: Session, pg_id: int) -> base_schemas.Attendance:
    attendance = db.query(models.Attendance).filter(models.Attendance.owner_id == pg_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="attendance not found")
    return attendance

def create_attendance(db: Session, attendance: base_schemas.AttendanceCreate):
    db_attendance = models.Attendance(
        owner_id=attendance.owner_id,
        email=attendance.email,
        location=attendance.location,
        schedule=attendance.schedule,
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def edit_attendance(
        db: Session, owner_id: int, attendance: base_schemas.AttendanceEdit
) -> base_schemas.Attendance:
    db_attendance = get_attendance(db, owner_id)
    update_data = attendance.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_attendance, key, value)

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance
