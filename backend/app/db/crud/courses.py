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

# def edit_post_graduation(
#         db: Session, post_graduation_id: int, course: base_schemas.PostGraduationEdit
# ) -> base_schemas.Course:
#     db_post_graduation = get_post_graduation(db, post_graduation_id)
#     update_data = course.dict(exclude_unset=True)
#     for key, value in update_data.items():
#         setattr(db_post_graduation, key, value)

#     db.add(db_post_graduation)
#     db.commit()
#     db.refresh(db_post_graduation)
#     return db_post_graduation
