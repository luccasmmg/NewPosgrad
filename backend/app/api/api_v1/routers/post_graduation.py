#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import (
    get_post_graduation_by_initials,
    get_post_graduation,
    create_post_graduation,
    edit_post_graduation,
    get_post_graduations,
    delete_post_graduation,
)
from app.schemas.base_schemas import PostGraduation, PostGraduationCreate, PostGraduationEdit
from app.core.auth import get_current_active_superuser

post_graduation_router = p = APIRouter()

@p.get(
    "/posgraduacao",
    response_model=t.List[PostGraduation],
    response_model_exclude_none=True,
)
async def post_graduations_list(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    post_graduations = get_post_graduations(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(post_graduations)}"
    return post_graduations

@p.get(
    "/posgraduacao/{post_id}",
    response_model=PostGraduation,
    response_model_exclude_none=True,
)
async def post_graduations_details(
        request: Request,
        post_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    post_graduation = get_post_graduation(db, post_id)
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
    "/posgraduacao/{post_id}",
    response_model=PostGraduation,
    response_model_exclude_none=True
)
async def post_graduation_edit(
        request: Request,
        id: str,
        post_graduation: PostGraduationEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_superuser),
):
    """
    Update an existing post graduation
    """
    return edit_post_graduation(db, id, post_graduation)

@p.delete(
    "/posgraduacao/{post_id}", response_model=PostGraduation, response_model_exclude_none=True
)
async def post_graduation_delete(
    request: Request,
    post_id: int,
    db=Depends(get_db),
    current_post_graduation=Depends(get_current_active_superuser),
):
    """
    Delete existing post_graduation
    """
    return delete_post_graduation(db, post_id)
