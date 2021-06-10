#!/usr/bin/env python3

from app.db import models

def test_add_participation(client, test_user, user_token_headers):
    new_participation = {
        "title": "Participação teste",
        "description": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "year": 2020,
        "category": "prize",
        "international": False
    }
    response = client.post(
        f"api/v1/participacao",
        json=new_participation,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_participation['id'] = 1
    new_participation['owner_id'] = test_user.owner_id
    assert response.json() == new_participation

def test_edit_participation(client, test_user, test_participation, user_token_headers):
    new_participation = {
        "title": "Participação teste 2",
        "description": "XXXXXXXXXXXXXX",
        "year": 2020,
        "category": "posdoc",
        "international": False
    }
    response = client.put(
        f"api/v1/participacao/{test_participation.id}",
        json=new_participation,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_participation['id'] = test_participation.id
    new_participation['owner_id'] = test_participation.owner_id
    assert response.json() == new_participation

def test_delete_participation(client, test_user, test_participation, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/participacao/{test_participation.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Participation).filter(models.Participation.deleted == False)) == []
