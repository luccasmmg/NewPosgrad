#!/usr/bin/env python3
from enum import Enum

from pydantic import BaseModel

from app.core.config import API_URL_ROOT

def to_camel(string: str) -> str:
    first, *others = string.split('_')
    return ''.join([first.lower()], *map(str.title, others))

class UrlEnum(str, Enum):
    published_articles = f'{API_URL_ROOT}curriculo-pesquisador/v1/artigos-publicados?'
    published_chapters = f'{API_URL_ROOT}curriculo-pesquisador/v1/capitulos-livros?'
    organized_books = f'{API_URL_ROOT}curriculo-pesquisador/v1/livros-publicados-organizados?'

class PublishedArticle(BaseModel):
    ano_producao: int
    issn: str
    local_publicacao: str
    natureza_producao: str
    nome_producao: str
    pais_producao: str
    pais_publicacao: str
    sequencia_producao: int
    titulo_periodico_revista: str
    volume: str

    class Config:
        alias_generator = to_camel

class Book(BaseModel):
    ano_producao: int
    cidade_editora: str
    isbn: str
    natureza_producao: str
    nome_editora: str
    nome_producao: str
    numero_edicao_revisao: str
    numero_volumes: str
    pais_producao: str
    pais_publicacao: str
    sequencia_producao: int
    tipo_producao: str

    class Config:
        alias_generator = to_camel

class PublishedBook(Book):
    pass

class PublishedBook(Book):
    pass
