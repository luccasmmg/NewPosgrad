#!/usr/bin/env python3

from fastapi import APIRouter, Request, Depends, Response, encoders
import typing as t
from pydantic import parse_obj_as
import asyncio
import aiohttp

from app.db.session import get_db
from app.db.crud.post_graduations import (
    get_post_graduation_by_initials,
)
from app.schemas.api_ufrn import Student, UrlEnum, Class
from app.core.api_ufrn import get_public_data, create_headers, get_public_data_async

api_sistemas_router = a = APIRouter()

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
    url_list = list(map(lambda p : f'{UrlEnum.students}id-curso={p.id_sigaa}', post_graduation.courses))
    list_of_functions = [get_public_data_async(i, client, headers) for i in url_list]

    students = [val for sublist in (await asyncio.gather(*list_of_functions)) for val in sublist]

    return parse_obj_as(t.List[Student], students)
