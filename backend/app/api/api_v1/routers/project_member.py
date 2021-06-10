#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import get_informations, delete_information, edit_information, get_information, create_project_member
from app.db import models as m

from app.schemas.pg_information_schemas import ProjectMemberCreate, ProjectMember, ProjectMemberEdit
from app.core.auth import get_current_active_user

project_member_router = p = APIRouter()

@p.get("/membro_projeto", response_model=t.List[ProjectMember], response_model_exclude_none=True)
async def get_project_members(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    project_members = get_informations(db, current_user.owner_id, m.ProjectMember).all()
    response.headers["Content-Range"] = f"0-9/{len(project_members)}"
    return project_members

@p.get("/membro_projeto/{project_member_id}", response_model=ProjectMember, response_model_exclude_none=True)
async def project_member_details(
        response: Response,
        project_member_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, project_member_id, m.ProjectMember)

@p.post("/membro_projeto", response_model=ProjectMember, response_model_exclude_none=True)
async def project_member_create(
    request: Request,
    project_member: ProjectMemberCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new project members
    """
    return create_project_member(db, current_user.owner_id, project_member)

@p.delete("/membro_projeto/{project_member_id}", response_model=ProjectMember, response_model_exclude_none=True)
async def project_member_delete(
        request: Request,
        project_member_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete project_member
    """
    return delete_information(db, get_information(db, project_member_id, m.ProjectMember).id, m.ProjectMember)

@p.put("/membro_projeto/{project_member_id}", response_model=ProjectMember, response_model_exclude_none=True)
async def project_member_edit(
        request: Request,
        project_member_id: int,
        project_member: ProjectMemberEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit project_member
    """
    return edit_information(db, get_information(db, project_member_id, m.ProjectMember).id, project_member, m.ProjectMember)
