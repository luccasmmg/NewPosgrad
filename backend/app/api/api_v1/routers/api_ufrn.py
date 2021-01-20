#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import (
    get_post_graduation_by_initials
)
from app.schemas.base_schemas import PostGraduation

api_sistemas_router = p = APIRouter()

@p.get(
    "/posgraduacao/{initials}",
    response_model=PostGraduation,
    response_model_exclude_none=True,
)
async def post_graduation_details(
        initials: str,
        db=Depends(get_db)
):
    """
    Get any post graduation details
    """
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return post_graduation
