#!/usr/bin/env python3

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import pg_information_schemas


def get_participations(db: Session, pg_id: int):
    print(type(models.Participation), flush=True)
    participations = db.query(models.Participation).filter(
        models.Participation.owner_id == pg_id).filter(models.Participation.deleted == False)
    return participations

def get_participation(db: Session, participation_id: int):
    participation = db.query(models.Participation).filter(
        models.Participation.id == participation_id).filter(models.Participation.deleted == False).first()
    return participation

def create_participation(db: Session, pg_id: int, participation: pg_information_schemas.ParticipationCreate):
    db_participation = models.Participation(
        owner_id=pg_id,
        title=participation.title,
        description=participation.description,
        year=participation.year,
        international=participation.international,
    )
    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)
    return db_participation

def delete_participation(db: Session, participation_id: int):
    participation = get_participation(db, participation_id)
    if not participation:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="participation not found")
    setattr(participation, "deleted", True)
    db.add(participation)
    db.commit()
    db.refresh(participation)
    return participation

def edit_participation(
        db: Session, participation_id: int, participation: pg_information_schemas.ParticipationEdit
) -> pg_information_schemas.Participation:
    db_participation = get_participation(db, participation_id)
    update_data = participation.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_participation, key, value)

    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)
    return db_participation
