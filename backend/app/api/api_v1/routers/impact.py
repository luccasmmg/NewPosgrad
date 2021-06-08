#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import get_informations, delete_information, edit_information, get_information, create_impact
from app.db import models as m

from app.schemas.pg_information_schemas import ImpactCreate, Impact, ImpactEdit
from app.core.auth import get_current_active_user

impact_router = i = APIRouter()

@i.get("/impacto", response_model=t.List[Impact], response_model_exclude_none=True)
async def get_impact(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    impacts = get_informations(db, current_user.owner_id, m.Impact).all()
    response.headers["Content-Range"] = f"0-9/{len(impacts)}"
    return impacts

@i.post("/impacto", response_model=Impact, response_model_exclude_none=True)
async def impact_create(
    request: Request,
    impact: ImpactCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create new impact
    """
    return create_impact(db, current_user.owner_id, impact)

@i.delete("/impacto/{impact_id}", response_model=Impact, response_model_exclude_none=True)
async def impact_delete(
        request: Request,
        impact_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete impact
    """
    return delete_information(db, get_information(db, impact_id, m.Impact).id, m.Impact)

@i.put("/impacto/{impact_id}", response_model=Impact, response_model_exclude_none=True)
async def impact_edit(
        request: Request,
        impact_id: int,
        impact: ImpactEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit impact
    """
    return edit_information(db, get_information(db, impact_id, m.Impact).id, impact, m.Impact)
