#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import (
    get_post_graduation_by_initials,
    create_post_graduation,
    edit_post_graduation
)
from app.schemas.base_schemas import PostGraduation, PostGraduationCreate, PostGraduationEdit
from app.core.auth import get_current_active_superuser

post_graduation_router = p = APIRouter()

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

@p.post(
    "/posgraduacao",
    response_model=PostGraduation,
    response_model_exclude_none=True
)
async def post_graduation_create(
        request: Request,
        post_graduation: PostGraduationCreate,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Create a post graduation
    """
    return create_post_graduation(db, post_graduation)

@p.put(
    "/posgraduacao/{initials}",
    response_model=PostGraduation,
    response_model_exclude_none=True
)
async def post_graduation_edit(
        request: Request,
        initials: str,
        post_graduation: PostGraduationEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Update an existing post graduation
    """
    post_graduation_id = get_post_graduation_by_initials(db, initials).id
    return edit_post_graduation(db, post_graduation_id, post_graduation)
