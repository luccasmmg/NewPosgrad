#!/usr/bin/env python3
from enum import Enum

from pydantic import BaseModel

from app.core.config import API_URL_ROOT

import typing as t

def to_camel(string: str) -> str:
    return ''.join(x.capitalize() or '_' for x in string.split('_'))

def to_kebab(string: str) -> str:
    return string.replace('_', '-')

class UrlEnum(str, Enum):
    published_articles = f'{API_URL_ROOT}curriculo-pesquisador/v1/artigos-publicados?'
    published_chapters = f'{API_URL_ROOT}curriculo-pesquisador/v1/capitulos-livros?'
    organized_books = f'{API_URL_ROOT}curriculo-pesquisador/v1/livros-publicados-organizados?'
    students = f'{API_URL_ROOT}discente/v1/discentes'
    classes = f'{API_URL_ROOT}turma/v1/turmas'

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
        alias_generator = to_kebab

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
        alias_generator = to_kebab

class PublishedBook(Book):
    pass

class PublishedBook(Book):
    pass

class Student(BaseModel):
    ano_ingresso: int = None
    cpf_cnpj: str = None
    descricao_forma_ingresso: str = None
    email: str = None
    id_curso: int =  None
    id_discente: int =  None
    id_forma_ingresso: int =  None
    id_gestora_academica: int =  None
    id_institucional: int =  None
    id_situacao_discente: int =  None
    id_tipo_discente: int =  None
    id_unidade: int =  None
    matricula: int =  None
    nome_curso: str = None
    nome_discente: str = None
    periodo_ingresso: int =  None
    sigla_nivel: str = None

    class Config:
        alias_generator = to_kebab

class Class(BaseModel):
    ano: int = None
    capacidade_aluno: int = None
    codigo_componente: str = None
    codigo_turma: str = None
    descricao_horario: str = None
    id_componente: int = None
    id_discente: int = None
    id_docente: int = None
    id_docente_externo: int = None
    id_situacao_turma: int = None
    id_turma: int = None
    id_turma_agrupadora: int = None
    id_unidade: int = None
    local: str = None
    nome_componente: str = None
    periodo: int = None
    sigla_nivel: str = None
    subturma: bool = None

    class Config:
        alias_generator = to_kebab
