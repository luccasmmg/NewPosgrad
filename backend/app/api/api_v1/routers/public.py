#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t
from pydantic import parse_obj_as
import asyncio
import aiohttp
import datetime

from app.db.session import get_db

from app.db.crud.post_graduations import get_post_graduation_by_initials, get_informations, get_information

from app.db import models as m

from app.schemas.api_ufrn import Student, UrlEnum, Class, PublishedArticle, OrganizedBook, PublishedChapter, SyllabusComponent
from app.schemas.base_schemas import PostGraduation
from app.schemas.pg_information_schemas import Researcher, Covenant, Participation, OfficialDocument, News, Event, ScheduledReport, StudentAdvisor, Staff
from app.schemas.scraping_schemas import Professor, NewsScraped, InstitutionalRepositoryDoc
from app.core.api_ufrn import get_public_data, create_headers, get_public_data_async
from app.scraping.professors_sigaa import get_professors_list
from app.scraping.news_sigaa import get_news_list
from app.scraping.institutional_repository import get_final_reports_list

public_router = p = APIRouter()

async def get_teacher(class_dict: dict, client: aiohttp.ClientSession, headers: dict):
    class_dict['docentes'] = await get_public_data_async(f'{UrlEnum.classes}/{class_dict["id-turma"]}/docentes', client, headers)
    return parse_obj_as(Class, class_dict)

async def get_publications(initials: str, enum_to_use: UrlEnum, db):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    researchers = list(get_informations(db, post_graduation.id, m.researcher))
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
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    students = get_public_data(f'{UrlEnum.students}?id-curso={id_course}')

    return parse_obj_as(t.List[Student], students)

@p.get(
    "/{initials}/disciplinas",
    response_model=t.List[SyllabusComponent],
)
async def syllabus_components(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    id_unit = get_post_graduation_by_initials(db, initials.upper()).id_unit
    syllabus_components = get_public_data(f'{UrlEnum.syllabus}?id-unidade={id_unit}&limit=100')

    return parse_obj_as(t.List[SyllabusComponent], syllabus_components)

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
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.Researcher))

@p.get(
    "/{initials}/convenios",
    response_model=t.List[Covenant]
)
async def covenants(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.Covenant))

@p.get(
    "/{initials}/participacoes",
    response_model=t.List[Participation]
)
async def participations(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.Participation))

@p.get(
    "/{initials}/documentos",
    response_model=t.List[OfficialDocument]
)
async def official_documents(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.OfficialDocument))

@p.get(
    "/{initials}/noticias",
    response_model=t.List[News]
)
async def news(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.News))

@p.get(
    "/{initials}/noticias_sigaa",
    response_model=t.List[NewsScraped]
)
async def news_sigaa(
        response: Response,
        initials: str,
        limit: int = 10,
        skip: int = 0,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return get_news_list(post_graduation, skip, limit)

@p.get(
    "/{initials}/eventos",
    response_model=t.List[Event]
)
async def events(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.Event))

@p.get(
    "/{initials}/equipe",
    response_model=t.List[Staff]
)
async def staff(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.Staff))

@p.get(
    "/{initials}/defesas",
    response_model=t.List[ScheduledReport]
)
async def scheduled_reports(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.ScheduledReport))

@p.get(
    "/{initials}/professores",
    response_model=t.List[Professor]
)
async def professors(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return get_professors_list(post_graduation)

@p.get(
    "/{initials}/orientadores",
    response_model=t.List[StudentAdvisor]
)
async def advisors(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(get_informations(db, post_graduation.id, m.StudentAdvisor))

@p.get(
    "/{initials}/{course_id}/repositorio_institucional",
    response_model=t.List[InstitutionalRepositoryDoc]
)
async def institutional_repository(
        response: Response,
        initials: str,
        course_id: int,
        db=Depends(get_db)
):
    course = get_information(db, course_id, m.Course)
    return get_final_reports_list(course)
