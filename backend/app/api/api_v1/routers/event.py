#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_event
from app.db import models as m

from app.schemas.pg_information_schemas import EventCreate, Event, EventEdit
from app.core.auth import get_current_active_user

event_router = e = APIRouter()

@e.post("/evento", response_model=Event, response_model_exclude_none=True)
async def event_create(
    request: Request,
    event: EventCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create new event
    """
    return create_event(db, current_user.owner_id, event)

@e.delete("/evento/{event_id}", response_model=Event, response_model_exclude_none=True)
async def event_delete(
        request: Request,
        event_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete event
    """
    return delete_information(db, get_information(db, event_id, m.Event).id, m.Event)

@e.put("/evento/{event_id}", response_model=Event, response_model_exclude_none=True)
async def event_edit(
        request: Request,
        event_id: int,
        event: EventEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit event
    """
    return edit_information(db, get_information(db, event_id, m.Event).id, event, m.Event)
