#!/usr/bin/env python3

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
    response = client.get(f"/api/v1/posgraduacao/PPGP/discentes/{test_course.id_sigaa}")
    print(response.json(), flush=True)
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())

def test_get_classes(client):
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
    response = client.get(f'api/v1/posgraduacao/PPGP/turmas/284?year=2020')
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())
