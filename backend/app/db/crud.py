from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models
from app.schemas import base_schemas
from app.core.security import get_password_hash


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> base_schemas.UserBase:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[base_schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: base_schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        first_name=user.first_name,
        owner_id=user.owner_id,
        last_name=user.last_name,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user


def edit_user(
    db: Session, user_id: int, user: base_schemas.UserEdit
) -> base_schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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
