#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import get_informations, delete_information, edit_information, get_information, create_project
from app.db import models as m

from app.schemas.pg_information_schemas import ProjectCreate, Project, ProjectEdit
from app.core.auth import get_current_active_user

project_router = p = APIRouter()

@p.get("/projeto", response_model=t.List[Project], response_model_exclude_none=True)
async def get_projects(
        response: Response,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    projects = get_informations(db, current_user.owner_id, m.Project).all()
    response.headers["Content-Range"] = f"0-9/{len(projects)}"
    return projects

@p.get("/projeto/{project_id}", response_model=Project, response_model_exclude_none=True)
async def project_details(
        response: Response,
        project_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    return get_information(db, project_id, m.Project)

@p.post("/projeto", response_model=Project, response_model_exclude_none=True)
async def project_create(
    request: Request,
    project: ProjectCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new projects
    """
    return create_project(db, current_user.owner_id, project)

@p.delete("/projeto/{project_id}", response_model=Project, response_model_exclude_none=True)
async def project_delete(
        request: Request,
        project_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete project
    """
    return delete_information(db, get_information(db, project_id, m.Project).id, m.Project)

@p.put("/projeto/{project_id}", response_model=Project, response_model_exclude_none=True)
async def project_edit(
        request: Request,
        project_id: int,
        project: ProjectEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit project
    """
    return edit_information(db, get_information(db, project_id, m.Project).id, project, m.Project)
