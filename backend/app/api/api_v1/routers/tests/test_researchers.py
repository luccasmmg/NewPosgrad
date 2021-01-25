#!/usr/bin/env python3

from app.db import models

def test_add_researcher(client, test_user, user_token_headers):
    new_researcher = {
        "name": "Maria Arlete",
        "cpf": "11111111111",
    }
    response = client.post(
        f"api/v1/pesquisador",
        json=new_researcher,
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_researcher.items())

def test_edit_researcher(client, test_user, test_researcher, user_token_headers):
    new_researcher = {
        "name": "Marconi Neves Macedo",
        "cpf": "11111111111",
    }
    response = client.put(
        f"api/v1/pesquisador/{test_researcher.id}",
        json=new_researcher,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_researcher['id'] = test_researcher.id
    new_researcher['owner_id'] = test_researcher.owner_id
    assert response.json() == new_researcher

def test_delete_researcher(client, test_user, test_researcher, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/pesquisador/{test_researcher.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Researcher).filter(models.Researcher.deleted == False)) == []
