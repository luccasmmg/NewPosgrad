#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3

from app.db.session import get_db
from app.db.crud.participations import (
    create_participation,
    get_participation,
    delete_participation,
    edit_participation
)
from app.schemas.pg_information_schemas import ParticipationCreate, Participation, ParticipationEdit
from app.core.auth import get_current_active_user

participation_router = p = APIRouter()

@p.post("/participacao", response_model=Participation, response_model_exclude_none=True)
async def participation_create(
    request: Request,
    participation: ParticipationCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new participations
    """
    return create_participation(db, current_user.owner_id, participation)

@p.delete("/participacao/{participation_id}", response_model=Participation, response_model_exclude_none=True)
async def participation_delete(
        request: Request,
        participation_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete participation
    """
    return delete_participation(db, get_participation(db, participation_id).id)

@p.put("/participacao/{participation_id}", response_model=Participation, response_model_exclude_none=True)
async def participation_edit(
        request: Request,
        participation_id: int,
        participation: ParticipationEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit participation
    """
    return edit_participation(db, get_participation(db, participation_id).id, participation)
