#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t
from pydantic import parse_obj_as
import asyncio
import aiohttp
import datetime

from app.db.session import get_db
from app.db.crud.post_graduations import (
    get_post_graduation_by_initials,
)
from app.schemas.api_ufrn import Student, UrlEnum, Class
from app.core.api_ufrn import get_public_data, create_headers, get_public_data_async

api_sistemas_router = a = APIRouter()

async def get_teacher(class_dict: dict, client: aiohttp.ClientSession, headers: dict):
    return dict(class_dict.keys() + get_public_data_async(f'{UrlEnum.classes}/{class_dict["id-turma"]}/docentes', client, headers).keys())

@a.get(
    "/posgraduacao/{initials}/discentes",
    response_model=t.List[Student],
)
async def students(
        response: Response,
        initials: str,
        db=Depends(get_db)
):
    """
    Get the students of a postgraduation
    """
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    post_graduation = get_post_graduation_by_initials(db, initials.upper())
    url_list = list(map(lambda p : f'{UrlEnum.students}?id-curso={p.id_sigaa}', post_graduation.courses))
    list_of_corroutines = [get_public_data_async(i, client, headers) for i in url_list]

    students = [val for sublist in (await asyncio.gather(*list_of_corroutines)) for val in sublist]

    return parse_obj_as(t.List[Student], students)

@a.get(
    "/posgraduacao/{initials}/turmas/{id_course}",
    response_model=t.List[Class]
)
async def classes(
        response: Response,
        initials: str,
        id_course: int,
        year: int = datetime.datetime.now().year,
        db=Depends(get_db)
):
    """
    Get the classes of a given course
    """
    client: ClientSession = aiohttp.ClientSession()
    headers: dict = create_headers()

    classes_without_teachers = list(get_public_data(f'{UrlEnum.classes}id-unidade={id_course}&ano={year}'))
    list_of_corroutines = [get_teacher(i, client, headers) for i in classes_without_teachers]

    classes = [val for sublist in (await asyncio.gather(*list_of_corroutines)) for val in sublist]

    return parse_obj_as(t.List[Class], classes)
