from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from .. import models
from app.schemas import pg_information_schemas


def get_covenants(db: Session, pg_id: int):
    covenants = db.query(models.Covenant).filter(models.Covenant.owner_id == pg_id).filter(models.Covenant.deleted == False)
    return covenants

def get_covenant(db: Session, covenant_id: int):
    covenant = db.query(models.Covenant).filter(models.Covenant.id == covenant_id).filter(models.Covenant.deleted == False).first()
    return covenant

def create_covenant(db: Session, pg_id: int, covenant: pg_information_schemas.CovenantCreate):
    db_covenant = models.Covenant(
        owner_id=pg_id,
        initials=covenant.initials,
        logo_file=covenant.logo_file,
        name=covenant.name,
    )
    db.add(db_covenant)
    db.commit()
    db.refresh(db_covenant)
    return db_covenant

def delete_covenant(db: Session, covenant_id: int):
    covenant = get_covenant(db, covenant_id)
    if not covenant:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="covenant not found")
    setattr(covenant, "deleted", True)
    db.add(covenant)
    db.commit()
    db.refresh(covenant)
    return covenant

def edit_covenant(
        db: Session, covenant_id: int, covenant: pg_information_schemas.CovenantEdit
) -> pg_information_schemas.Covenant:
    db_covenant = get_covenant(db, covenant_id)
    update_data = covenant.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_covenant, key, value)

    db.add(db_covenant)
    db.commit()
    db.refresh(db_covenant)
    return db_covenant
