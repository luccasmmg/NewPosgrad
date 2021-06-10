#!/usr/bin/env python3

from app.db import models

def test_add_repository_docs(client, test_user, user_token_headers):
    new_repository_docs = {
        "title": "string",
        "author": "string",
        "year": 1,
        "link": "https://google.com"
    }
    response = client.post(
        f"api/v1/repositorio",
        json=new_repository_docs,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_repository_docs['id'] = 1
    new_repository_docs['owner_id'] = test_user.owner_id
    assert response.json() == new_repository_docs

def test_edit_repository_docs(client, test_user, test_repository_docs, user_token_headers):
    new_repository_docs = {
        "title": "string 2",
        "author": "string 2",
        "year": 2,
        "link": "https://google2.com"
    }
    response = client.put(
        f"api/v1/repositorio/{test_repository_docs.id}",
        json=new_repository_docs,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_repository_docs['id'] = test_repository_docs.id
    new_repository_docs['owner_id'] = test_repository_docs.owner_id
    assert response.json() == new_repository_docs

def test_delete_repository_docs(client, test_user, test_repository_docs, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/repositorio/{test_repository_docs.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Repository).filter(models.Repository.deleted == False)) == []
