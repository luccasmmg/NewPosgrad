#!/usr/bin/env python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import base_schemas

def get_course(db: Session, course_id: int) -> base_schemas.Course:
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

def create_course(db: Session, course: base_schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        owner_id=course.owner_id,
        id_sigaa=course.id_sigaa,
        course_type=course.course_type
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    course = get_course(db, course_id)
    if not course:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Course not found")
    db.delete(course)
    db.commit()
    return course

def edit_course(
        db: Session, course_id: int, course: base_schemas.CourseEdit
) -> base_schemas.Course:
    db_course = get_course(db, course_id)
    update_data = course.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_course, key, value)

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
