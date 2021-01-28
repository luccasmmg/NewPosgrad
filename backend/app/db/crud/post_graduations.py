#!/usr/bin/env python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t
import enum

from .. import models
from app.schemas import base_schemas
from app.schemas import pg_information_schemas

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

def get_informations(db: Session, pg_id: int, model):
    informations = db.query(model).filter(
        model.owner_id == pg_id).filter(model.deleted == False)
    return informations

def get_information(db: Session, information_id: int, model):
    information = db.query(model).filter(
        model.id == information_id).filter(model.deleted == False).first()
    return information

def delete_information(db: Session, information_id: int, model):
    information = get_information(db, information_id, model)
    if not information:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="information not found")
    setattr(information, "deleted", True)
    db.add(information)
    db.commit()
    db.refresh(information)
    return information

def edit_information(db: Session, information_id: int, information, model):
    db_information = get_information(db, information_id, model)
    update_data = information.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_information, key, value)

    db.add(db_information)
    db.commit()
    db.refresh(db_information)
    return db_information

def add_information(db: Session, model):
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def create_researcher(db: Session, pg_id: int, researcher: pg_information_schemas.ResearcherCreate):
    db_researcher = models.Researcher(
        owner_id=pg_id,
        cpf=researcher.cpf,
        name=researcher.name,
    )
    return add_information(db, db_researcher)
