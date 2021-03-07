#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders, Form, File, UploadFile, HTTPException
import typing as t
import boto3

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, get_informations, create_participation
from app.db import models as m

from app.schemas.pg_information_schemas import ParticipationCreate, Participation, ParticipationEdit
from app.core.auth import get_current_active_user

participation_router = p = APIRouter()

@p.get("/participacao", response_model=t.List[Participation], response_model_exclude_none=True)
async def get_participations(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    participations = get_informations(db, current_user.owner_id, m.Participation).all()
    response.headers["Content-Range"] = f"0-9/{len(participations)}"
    return participations

@p.get("/participacao/{participation_id}", response_model=Participation, response_model_exclude_none=True)
async def participation_details(
        response: Response,
        participation_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, participation_id, m.Participation)

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
    return delete_information(db, get_information(db, participation_id, m.Participation).id, m.Participation)

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
    return edit_information(db, get_information(db, participation_id, m.Participation).id, participation, m.Participation)
