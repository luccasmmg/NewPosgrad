#!/usr/bin/env python3

def test_get_event_works(client, test_pg, test_researcher):
    dummy_dict = {
        "ano-producao": 0,
        "isbn": "string",
        "natureza-producao": "string",
        "nome-evento": "string",
        "nome-producao": "string",
        "pais-evento": "string",
        "pais-producao": "string",
        "sequencia-producao": 0,
        "titulo-anais": "string",
        "volume": "string",
        "autores": [
        {
            "nome": "string",
            "nome-citacao": "string",
            "ordem-autoria": "string"
        }
        ]
    }
    response = client.get(f"/api/v1/publico/PPGP/trabalhos_eventos")
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())

def test_get_students(client, test_course):
    dummy_dict = {
        "ano-ingresso": 0,
        "cpf-cnpj": "string",
        "descricao-forma-ingresso": "string",
        "email": "string",
        "id-curso": 0,
        "id-discente": 0,
        "id-forma-ingresso": 0,
        "id-gestora-academica": 0,
        "id-institucional": 0,
        "id-situacao-discente": 0,
        "id-tipo-discente": 0,
        "id-unidade": 0,
        "matricula": 0,
        "nome-curso": "string",
        "nome-discente": "string",
        "periodo-ingresso": 0,
        "sigla-nivel": "string"
    }
    response = client.get(f"/api/v1/publico/PPGP/discentes/{test_course.id_sigaa}")
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())

def test_get_classes(client, test_pg):
    dummy_dict = {
        "ano": 0,
        "capacidade-aluno": 0,
        "codigo-componente": "string",
        "codigo-turma": "string",
        "descricao-horario": "string",
        "id-componente": 0,
        "id-discente": 0,
        "id-docente": 0,
        "id-docente-externo": 0,
        "id-situacao-turma": 0,
        "id-turma": 0,
        "id-turma-agrupadora": 0,
        "id-unidade": 0,
        "local": "string",
        "nome-componente": "string",
        "periodo": 0,
        "sigla-nivel": "string",
        "subturma": True,
        "docentes": [
        {
            "ch-dedicada-periodo": 0,
            "cpf": 0,
            "id-docente": 0,
            "id-docente-externo": 0,
            "nome-docente": "string"
        }
        ]
    }
    response = client.get(f'api/v1/publico/PPGP/turmas')
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())

def test_get_syllabus(client, test_pg):
    dummy_dict = {
        "carga-horaria-total": 0,
        "co-requisitos": "string",
        "codigo": "string",
        "departamento": "string",
        "descricao-tipo-atividade": "string",
        "equivalentes": "string",
        "id-componente": 0,
        "id-matriz-curricular": 0,
        "id-tipo-atividade": 0,
        "id-tipo-componente": 0,
        "id-unidade": 0,
        "nivel": "string",
        "nome": "string",
        "pre-requisitos": "string",
        "semestre-oferta": 0
    }
    response = client.get(f'api/v1/publico/PPGP/disciplinas')
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())
