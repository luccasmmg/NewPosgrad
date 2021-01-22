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
    response = client.get(f"/api/v1/posgraduacao/PPGP/discentes")
    assert response.status_code == 200
    assert all(key in response.json()[0].keys() for key in dummy_dict.keys())
