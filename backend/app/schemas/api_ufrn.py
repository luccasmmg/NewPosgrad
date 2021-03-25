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
    published_articles = f'{API_URL_ROOT}curriculo-pesquisador/v1/artigos-publicados'
    published_chapters = f'{API_URL_ROOT}curriculo-pesquisador/v1/capitulos-livros'
    organized_books = f'{API_URL_ROOT}curriculo-pesquisador/v1/livros-publicados-organizados'
    event_works = f'{API_URL_ROOT}curriculo-pesquisador/v1/trabalhos-eventos'
    students = f'{API_URL_ROOT}discente/v1/discentes'
    classes = f'{API_URL_ROOT}turma/v1/turmas'
    syllabus = f'{API_URL_ROOT}curso/v1/componentes-curriculares'

class Author(BaseModel):
    nome: str = None
    nome_citacao: str = None
    ordem_autoria: str = None

    class Config:
        alias_generator = to_kebab

class PublishedArticle(BaseModel):
    ano_producao: int = None
    issn: str = None
    local_publicacao: str = None
    natureza_producao: str = None
    nome_producao: str = None
    pais_producao: str = None
    pais_publicacao: str = None
    sequencia_producao: int = None
    titulo_periodico_revista: str = None
    volume: str = None
    autores: t.List[Author] = None

    class Config:
        alias_generator = to_kebab

class EventWork(BaseModel):
    ano_producao: int = None
    isbn: str = None
    natureza_producao: str = None
    nome_evento: str = None
    nome_producao: str = None
    pais_evento: str = None
    pais_producao: str = None
    sequencia_producao: int = None
    titulo_anais: str = None
    volume: str = None
    autores: t.List[Author] = None

    class Config:
        alias_generator = to_kebab

class Book(BaseModel):
    ano_producao: int = None
    cidade_editora: str = None
    isbn: str = None
    natureza_producao: str = None
    nome_editora: str = None
    nome_producao: str = None
    numero_edicao_revisao: str = None
    numero_volumes: str = None
    pais_producao: str = None
    pais_publicacao: str = None
    sequencia_producao: int = None
    tipo_producao: str = None
    autores: t.List[Author] = None

    class Config:
        alias_generator = to_kebab

class OrganizedBook(Book):
    pass

class PublishedChapter(Book):
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

class Teacher(BaseModel):
  ch_dedicada_periodo: int = None
  cpf: int = None
  id_docente: int = None
  id_docente_externo: int = None
  nome_docente: str = None

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
    docentes: t.List[Teacher] = []

    class Config:
        alias_generator = to_kebab

class SyllabusComponent(BaseModel):
    carga_horaria_total: int = None
    co_requisitos: str = None
    codigo: str  = None
    departamento: str  = None
    descricao_tipo_atividade: str  = None
    disciplina_obrigatoria: bool = None
    equivalentes: str  = None
    id_componente:  int = None
    id_matriz_curricular:  int = None
    id_tipo_atividade:  int = None
    id_tipo_componente:  int = None
    id_unidade:  int = None
    nivel: str  = None
    nome: str  = None
    pre_requisitos: str  = None
    semestre_oferta:  int = None

    class Config:
        alias_generator = to_kebab
