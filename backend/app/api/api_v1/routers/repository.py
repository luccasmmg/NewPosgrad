#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import get_informations, delete_information, edit_information, get_information, create_repository_doc
from app.db import models as m

from app.schemas.pg_information_schemas import RepositoryDocCreate, RepositoryDoc, RepositoryDocEdit
from app.core.auth import get_current_active_user

repository_doc_router = r = APIRouter()

@r.get("/repositorio", response_model=t.List[RepositoryDoc], response_model_exclude_none=True)
async def get_repository_docs(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    repository_docs = get_informations(db, current_user.owner_id, m.Repository).all()
    response.headers["Content-Range"] = f"0-9/{len(repository_docs)}"
    return repository_docs

@r.get("/repositorio/{repository_doc_id}", response_model=RepositoryDoc, response_model_exclude_none=True)
async def repository_doc_details(
        response: Response,
        repository_doc_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, repository_doc_id, m.Repository)

@r.post("/repositorio", response_model=RepositoryDoc, response_model_exclude_none=True)
async def repository_doc_create(
    request: Request,
    RepositoryDoc: RepositoryDocCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create new RepositoryDoc
    """
    return create_repository_doc(db, current_user.owner_id, RepositoryDoc)

@r.delete("/repositorio/{repository_doc_id}", response_model=RepositoryDoc, response_model_exclude_none=True)
async def repository_doc_delete(
        request: Request,
        repository_doc_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete RepositoryDoc
    """
    return delete_information(db, get_information(db, repository_doc_id, m.Repository).id, m.Repository)

@r.put("/repositorio/{repository_doc_id}", response_model=RepositoryDoc, response_model_exclude_none=True)
async def repository_doc_edit(
        request: Request,
        repository_doc_id: int,
        RepositoryDoc: RepositoryDocEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit RepositoryDoc
    """
    return edit_information(db, get_information(db, repository_doc_id, m.Repository).id, RepositoryDoc, m.Repository)
