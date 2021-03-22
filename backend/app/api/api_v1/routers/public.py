#!/usr/bin/env python3

from fastapi import APIRouter, Depends, Response, encoders
from starlette.requests import Request
import typing as t
from pydantic import parse_obj_as
import asyncio
import aiohttp
import datetime

from app.db.session import get_db

from app.db.crud.post_graduations import get_post_graduations, get_post_graduation_by_initials, get_informations, get_information

from app.db import models as m

from app.schemas.api_ufrn import Student, UrlEnum, Class, PublishedArticle, OrganizedBook, PublishedChapter, SyllabusComponent
from app.schemas.base_schemas import PostGraduation
from app.schemas.pg_information_schemas import Researcher, Covenant, Participation, OfficialDocument, News, Event, ScheduledReport, StudentAdvisor, Staff
from app.schemas.scraping_schemas import Professor, NewsScraped, InstitutionalRepositoryDoc
from app.core.api_ufrn import get_public_data, create_headers, get_public_data_async
from app.scraping.professors_sigaa import get_professors_list
from app.scraping.news_sigaa import get_news_list
from app.scraping.institutional_repository import get_final_reports_list

from fastapi_cache.decorator import cache
from fastapi_cache.coder import JsonCoder

public_router = p = APIRouter()

async def get_teacher(class_dict: dict, client: aiohttp.ClientSession, headers: dict):
    class_dict['docentes'] = await get_public_data_async(f'{UrlEnum.classes}/{class_dict["id-turma"]}/docentes', client, headers)
    return parse_obj_as(Class, class_dict)

async def get_authors(publication_dict: dict, enum_to_use: UrlEnum, client: aiohttp.ClientSession, headers: dict):
    publication_dict['autores'] = await get_public_data_async(f'{enum_to_use}/{publication_dict["sequencia-producao"]}/autores?cpf-cnpj-pesquisador={publication_dict["autores"]}', client, headers)
    return publication_dict

async def get_publications(initials: str, enum_to_use: UrlEnum, db):
    async def get_publications_by_cpf(enum_to_use: UrlEnum, cpf: str, client: aiohttp.ClientSession, headers: dict):
        def add_cpf(x, cpf):
            new_dict = x
            new_dict['autores'] = cpf
            return new_dict

        publications = await get_public_data_async(f"{enum_to_use}?cpf-cnpj={cpf}&limit=100", client, headers)
        publications_with_cpf = map(lambda x: add_cpf(x, cpf), publications)
        return publications_with_cpf
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    researchers = list(get_informations(db, post_graduation.id, m.Researcher))
    list_of_corroutines = [get_publications_by_cpf(enum_to_use, i.cpf, client, headers) for i in researchers]

    return [item for sublist in await asyncio.gather(*list_of_corroutines) for item in sublist]

@p.get(
    "/",
    response_model=t.List[PostGraduation],
    response_model_exclude_none=True,
)
async def post_graduations(
        db=Depends(get_db),
):
    post_graduations = get_post_graduations(db)
    return post_graduations

@p.get(
    "/{initials}",
    response_model=PostGraduation,
    response_model_exclude_none=True,
)
@cache(expire=60)
async def post_graduation_details(
        initials: str,
        request: Request = None,
        db=Depends(get_db),
):
    post_graduation = PostGraduation.from_orm(get_post_graduation_by_initials(db, initials.upper())).dict()
    return post_graduation

@p.get(
    "/{initials}/artigos",
    response_model=t.List[PublishedArticle]
)
async def articles(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):

    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    articles = await get_publications(initials, UrlEnum.published_articles, db)
    filteredArticles = list(filter(lambda x: int(x['ano-producao']) > (datetime.datetime.now().year - 4), articles))
    list_of_corroutines = [get_authors(i, UrlEnum.published_articles, client, headers) for i in filteredArticles]
    articlesWithAuthors = await asyncio.gather(*list_of_corroutines)

    return parse_obj_as(t.List[PublishedArticle], articlesWithAuthors)

@p.get(
    "/{initials}/livros",
    response_model=t.List[OrganizedBook]
)
async def books(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    books = await get_publications(initials, UrlEnum.organized_books, db)
    filteredBooks = list(filter(lambda x: int(x['ano-producao']) > (datetime.datetime.now().year - 4), books))
    list_of_corroutines = [get_authors(i, UrlEnum.organized_books, client, headers) for i in filteredBooks]
    booksWithAuthors = await asyncio.gather(*list_of_corroutines)

    return parse_obj_as(t.List[OrganizedBook], booksWithAuthors)

@p.get(
    "/{initials}/capitulos",
    response_model=t.List[PublishedChapter]
)
async def chapters(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    chapters = await get_publications(initials, UrlEnum.published_chapters, db)
    filteredChapters = list(filter(lambda x: int(x['ano-producao']) > (datetime.datetime.now().year - 4), chapters))
    list_of_corroutines = [get_authors(i, UrlEnum.published_chapters, client, headers) for i in filteredChapters]
    chaptersWithAuthors = await asyncio.gather(*list_of_corroutines)

    return parse_obj_as(t.List[PublishedChapter], chaptersWithAuthors)

@p.get(
    "/{initials}/discentes/{id_sigaa}",
    response_model=t.List[Student],
)
async def students(
        response: Response,
        initials: str,
        id_sigaa: int,
        db=Depends(get_db)
):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    students = get_public_data(f'{UrlEnum.students}?id-curso={id_sigaa}')

    return parse_obj_as(t.List[Student], students)

@p.get(
    "/{initials}/disciplinas",
    response_model=t.List[SyllabusComponent],
)
async def syllabus_components(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    id_unit = get_post_graduation_by_initials(db, initials.upper()).id_unit
    syllabus_components = get_public_data(f'{UrlEnum.syllabus}?id-unidade={id_unit}&limit=100')

    return syllabus_components

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
@cache(expire=60)
async def researchers(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: Researcher.from_orm(x).dict(), get_informations(db, post_graduation.id, m.Researcher)))

@p.get(
    "/{initials}/convenios",
    response_model=t.List[Covenant]
)
@cache(expire=60)
async def covenants(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: Covenant.from_orm(x).dict(), get_informations(db, post_graduation.id, m.Covenant)))

@p.get(
    "/{initials}/participacoes",
    response_model=t.List[Participation]
)
@cache(expire=60)
async def participations(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: Participation.from_orm(x).dict(), get_informations(db, post_graduation.id, m.Participation)))

@p.get(
    "/{initials}/documentos",
    response_model=t.List[OfficialDocument]
)
@cache(expire=60)
async def official_documents(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: OfficialDocument.from_orm(x).dict(), get_informations(db, post_graduation.id, m.OfficialDocument)))

@p.get(
    "/{initials}/noticias",
    response_model=t.List[News]
)
@cache(expire=60)
async def news(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: News.from_orm(x).dict(), get_informations(db, post_graduation.id, m.News)))

@p.get(
    "/{initials}/noticias_sigaa",
    response_model=t.List[NewsScraped]
)
@cache(expire=60)
async def news_sigaa(
        initials: str,
        request: Request = None,
        limit: int = 10,
        skip: int = 0,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: x.dict(), get_news_list(post_graduation, skip, limit)))

@p.get(
    "/{initials}/eventos",
    response_model=t.List[Event]
)
@cache(expire=60)
async def events(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: Event.from_orm(x).dict(), get_informations(db, post_graduation.id, m.Event)))

@p.get(
    "/{initials}/equipe",
    response_model=t.List[Staff]
)
@cache(expire=60)
async def staff(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: Staff.from_orm(x).dict(), get_informations(db, post_graduation.id, m.Staff)))

@p.get(
    "/{initials}/defesas",
    response_model=t.List[ScheduledReport]
)
@cache(expire=60)
async def scheduled_reports(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: ScheduledReport.from_orm(x).dict(), get_informations(db, post_graduation.id, m.ScheduledReport)))

@p.get(
    "/{initials}/professores",
    response_model=t.List[Professor]
)
@cache(expire=60)
async def professors(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: x.dict(), get_professors_list(post_graduation)))

@p.get(
    "/{initials}/orientadores",
    response_model=t.List[StudentAdvisor]
)
@cache(expire=60)
async def advisors(
        initials: str,
        request: Request = None,
        db=Depends(get_db)
):
    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    return list(map(lambda x: StudentAdvisor.from_orm(x).dict(), get_informations(db, post_graduation.id, m.StudentAdvisor)))

@p.get(
    "/{initials}/{course_id}/repositorio_institucional",
    response_model=t.List[InstitutionalRepositoryDoc]
)
@cache(expire=60)
async def institutional_repository(
        initials: str,
        course_id: int,
        request: Request = None,
        db=Depends(get_db)
):
    course = get_information(db, course_id, m.Course)
    return list(map(lambda x: x.dict(), get_final_reports_list(course)))
