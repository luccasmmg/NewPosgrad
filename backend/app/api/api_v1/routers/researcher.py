from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_researcher
from app.db import models as m

from app.schemas.pg_information_schemas import ResearcherCreate, Researcher, ResearcherEdit
from app.core.auth import get_current_active_user

researcher_router = r = APIRouter()

@r.post("/pesquisador", response_model=Researcher, response_model_exclude_none=True)
async def researcher_create(
    request: Request,
    researcher: ResearcherCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new researchers
    """
    return create_researcher(db, current_user.owner_id, researcher)

@r.delete("/pesquisador/{researcher_id}", response_model=Researcher, response_model_exclude_none=True)
async def researcher_delete(
        request: Request,
        researcher_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete researcher
    """
    return delete_information(db, get_information(db, researcher_id, m.Researcher).id, m.Researcher)

@r.put("/pesquisador/{researcher_id}", response_model=Researcher, response_model_exclude_none=True)
async def researcher_edit(
        request: Request,
        researcher_id: int,
        researcher: ResearcherEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit researcher
    """
    return edit_information(db, get_information(db, researcher_id, m.Researcher).id, researcher, m.Researcher)
