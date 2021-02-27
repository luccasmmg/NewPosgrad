#!/usr/bin/env python3
from pydantic import BaseModel, HttpUrl
from datetime import date

class Professor(BaseModel):
    name: str
    rank: str
    level: str
    phone: str
    lattes: str
    email: str

class NewsScraped(BaseModel):
    title: str
    date: date
    body: str
    url: HttpUrl = None

class InstitutionalRepositoryDoc(BaseModel):
    title: str
    authors: str
    keywords: str
    issue_date: str
    publisher: str
    citation: str
    portuguese_abstract: str
    abstract: str
    uri: HttpUrl
