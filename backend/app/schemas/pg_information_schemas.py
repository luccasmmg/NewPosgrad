#!/usr/bin/env python3

from pydantic import BaseModel

import typing as t

class ResearcherBase(BaseModel):
    cpf: str
    name: str

class ResearcherCreate(ResearcherBase):
    pass

class ResearcherEdit(ResearcherBase):
    pass

class Researcher(ResearcherBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class CovenantBase(BaseModel):
    name: str
    initials: str

class CovenantCreate(CovenantBase):
    logo_file: str
    pass

class CovenantEdit(CovenantBase):
    pass

class Covenant(CovenantBase):
    logo_file: str
    id: int
    owner_id: int

    class Config:
        orm_mode = True
