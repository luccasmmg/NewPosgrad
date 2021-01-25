from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import pg_information_schemas


def get_researchers(db: Session, pg_id: int):
    researchers = db.query(models.Researcher).filter(models.Researcher.owner_id == pg_id and models.Researcher.deleted == False)
    return researchers

def get_researcher(db: Session, researcher_id: int):
    researcher = db.query(models.Researcher).filter(models.Researcher.id == researcher_id).first()
    return researcher

def create_researcher(db: Session, pg_id: int, researcher: pg_information_schemas.ResearcherCreate):
    db_researcher = models.Researcher(
        owner_id=pg_id,
        cpf=researcher.cpf,
        name=researcher.name,
    )
    db.add(db_researcher)
    db.commit()
    db.refresh(db_researcher)
    return db_researcher

def delete_researcher(db: Session, researcher_id: int):
    researcher = get_researcher(db, researcher_id)
    if not researcher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Researcher not found")
    db.delete(researcher)
    db.commit()
    return researcher

def edit_researcher(
        db: Session, researcher_id: int, researcher: pg_information_schemas.ResearcherEdit
) -> pg_information_schemas.Researcher:
    db_researcher = get_researcher(db, researcher_id)
    update_data = researcher.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_researcher, key, value)

    db.add(db_researcher)
    db.commit()
    db.refresh(db_researcher)
    return db_researcher
