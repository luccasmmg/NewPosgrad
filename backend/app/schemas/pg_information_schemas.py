#!/usr/bin/env python3

from pydantic import BaseModel

from app.db.models import DocumentCategory

import typing as t

import datetime

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

#Covenant schemas

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

#Participation schemas

class ParticipationBase(BaseModel):
    title: str
    description: str = ""
    year: int = None
    international: bool = False

class ParticipationCreate(ParticipationBase):
    pass

class ParticipationEdit(ParticipationBase):
    pass

class Participation(ParticipationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#Official Document

class OfficialDocumentBase(BaseModel):
    title: str
    cod: str
    category: DocumentCategory

class OfficialDocumentCreate(OfficialDocumentBase):
    file: str
    pass

class OfficialDocumentEdit(OfficialDocumentBase):
    pass

class OfficialDocument(OfficialDocumentBase):
    id: int
    owner_id: int
    inserted_on: datetime.datetime

    class Config:
        orm_mode = True
