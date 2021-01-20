#!/usr/bin/env python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import base_schemas

def get_post_graduation(db: Session, post_graduation_id: int) -> base_schemas.PostGraduation:
    post_graduation = db.query(models.PostGraduation).filter(models.PostGraduation.id == post_graduation_id).first()
    if not post_graduation:
        raise HTTPException(status_code=404, detail="Post Graduation not found")
    return post_graduation

def get_post_graduation_by_initials(db: Session, initials: str) -> base_schemas.PostGraduation:
    post_graduation = db.query(models.PostGraduation).filter(models.PostGraduation.initials == initials).first()
    if not post_graduation:
        raise HTTPException(status_code=404, detail="Post Graduation not found")
    return post_graduation

def create_post_graduation(db: Session, post_graduation: base_schemas.PostGraduationCreate):
    db_post_graduation = models.PostGraduation(
        id_unit=post_graduation.id_unit,
        name=post_graduation.name,
        initials=post_graduation.initials,
        sigaa_code=post_graduation.sigaa_code,
        is_signed_in=post_graduation.is_signed_in,
        old_url=post_graduation.old_url,
        description_small=post_graduation.description_small,
        description_big=post_graduation.description_big,
    )
    db.add(db_post_graduation)
    db.commit()
    db.refresh(db_post_graduation)
    return db_post_graduation

def edit_post_graduation(
        db: Session, post_graduation_id: int, post_graduation: base_schemas.PostGraduationEdit
) -> base_schemas.PostGraduation:
    db_post_graduation = get_post_graduation(db, post_graduation_id)
    update_data = post_graduation.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post_graduation, key, value)

    db.add(db_post_graduation)
    db.commit()
    db.refresh(db_post_graduation)
    return db_post_graduation
