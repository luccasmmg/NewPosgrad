#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t
from pydantic import parse_obj_as
import asyncio
import aiohttp
import datetime

from app.db.session import get_db

from app.db.crud.post_graduations import get_post_graduation_by_initials
from app.db.crud.researchers import get_researchers
from app.db.crud.covenants import get_covenants

from app.schemas.api_ufrn import Student, UrlEnum, Class, PublishedArticle, OrganizedBook, PublishedChapter
from app.schemas.base_schemas import PostGraduation
from app.schemas.pg_information_schemas import Researcher, Covenant
from app.core.api_ufrn import get_public_data, create_headers, get_public_data_async

public_router = p = APIRouter()

async def get_teacher(class_dict: dict, client: aiohttp.ClientSession, headers: dict):
    class_dict['docentes'] = await get_public_data_async(f'{UrlEnum.classes}/{class_dict["id-turma"]}/docentes', client, headers)
    return parse_obj_as(Class, class_dict)

async def get_publications(initials: str, enum_to_use: UrlEnum, db):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    researchers = list(get_researchers(db, post_graduation.id))
    list_of_corroutines = [get_public_data_async(f"{enum_to_use}cpf-cnpj={i.cpf}", client, headers) for i in researchers]

    return [item for sublist in await asyncio.gather(*list_of_corroutines) for item in sublist]

@p.get(
    "/{initials}",
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

@p.get(
    "/{initials}/artigos",
    response_model=t.List[PublishedArticle]
)
async def articles(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the articles published by researchers of a given course
    """
    articles = await get_publications(initials, UrlEnum.published_articles, db)
    return parse_obj_as(t.List[PublishedArticle], articles)

@p.get(
    "/{initials}/livros",
    response_model=t.List[OrganizedBook]
)
async def books(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the books published by researchers of a given course
    """
    books = await get_publications(initials, UrlEnum.organized_books, db)
    return parse_obj_as(t.List[OrganizedBook], books)

@p.get(
    "/{initials}/capitulos",
    response_model=t.List[OrganizedBook]
)
async def chapters(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the chapters of books published by researchers of a given course
    """
    chapters = await get_publications(initials, UrlEnum.published_chapters , db)
    return parse_obj_as(t.List[PublishedChapter], chapters)

@p.get(
    "/{initials}/discentes/{id_course}",
    response_model=t.List[Student],
)
async def students(
        response: Response,
        initials: str,
        id_course: int,
        db=Depends(get_db)
):
    """
    Get the students of a postgraduation
    """
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    students = get_public_data(f'{UrlEnum.students}?id-curso={id_course}')

    return parse_obj_as(t.List[Student], students)

@p.get(
    "/{initials}/turmas/{id_course}",
    response_model=t.List[Class]
)
async def classes(
        response: Response,
        initials: str,
        id_course: int,
        year: int = datetime.datetime.now().year,
):
    """
    Get the classes of a given course
    """
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    classes_without_teachers = list(get_public_data(f'{UrlEnum.classes}?id-unidade={id_course}&ano={year}'))
    list_of_corroutines = [get_teacher(i, client, headers) for i in classes_without_teachers]

    classes = await asyncio.gather(*list_of_corroutines)
    return list(classes)

@p.get(
    "/{initials}/pesquisadores",
    response_model=t.List[Researcher]
)
async def researchers(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the researchers
    """
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_researchers(db, post_graduation.id))

@p.get(
    "/{initials}/convenios",
    response_model=t.List[Covenant]
)
async def covenants(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the covenants
    """
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_covenants(db, post_graduation.id))
