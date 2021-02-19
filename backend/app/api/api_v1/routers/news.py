#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t

from app.db.session import get_db
from app.db.crud.post_graduations import delete_information, edit_information, get_information, create_news
from app.db import models as m

from app.schemas.pg_information_schemas import NewsCreate, News, NewsEdit
from app.core.auth import get_current_active_user

news_router = n = APIRouter()

@n.post("/noticia", response_model=News, response_model_exclude_none=True)
async def news_create(
    request: Request,
    news: NewsCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create new news(lol)
    """
    return create_news(db, current_user.owner_id, news)

@n.delete("/noticia/{news_id}", response_model=News, response_model_exclude_none=True)
async def news_delete(
        request: Request,
        news_id: int,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Delete news
    """
    return delete_information(db, get_information(db, news_id, m.News).id, m.News)

@n.put("/noticia/{news_id}", response_model=News, response_model_exclude_none=True)
async def news_edit(
        request: Request,
        news_id: int,
        news: NewsEdit,
        db=Depends(get_db),
        current_user=Depends(get_current_active_user),
):
    """
    Edit news
    """
    return edit_information(db, get_information(db, news_id, m.News).id, news, m.News)
