#!/usr/bin/env python3
from app.db import models

def test_get_projects(client, test_researcher, test_user, user_token_headers, test_project):
    response = client.get(
        f"api/v1/projeto",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_one_project(client, test_researcher, test_project, test_user, user_token_headers):
    response = client.get(
        f"api/v1/projeto/{test_project.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert response.json()['id'] == test_project.id

def test_add_project(client, test_user, test_researcher, user_token_headers):
    new_project = {
        "coordinator": test_researcher.id,
        "name": "string",
        "status": "string",
        "year": 2020,
        "email": "string"
    }
    response = client.post(
        f"api/v1/projeto",
        json=new_project,
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_project.items())

def test_edit_project(client, test_user, test_project, test_researcher, user_token_headers):
    new_project = {
        "coordinator": test_researcher.id,
        "name": "string 2",
        "status": "string 2",
        "year": 2020,
        "email": "string"
    }
    response = client.put(
        f"api/v1/projeto/{test_project.id}",
        json=new_project,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_project['id'] = test_project.id
    new_project['owner_id'] = test_project.owner_id
    new_project['coordinator_data'] = {
      "cpf": test_researcher.cpf,
      "name": test_researcher.name,
      "id": test_researcher.id,
      "owner_id": test_researcher.owner_id
    }
    new_project['members'] = []
    assert response.json() == new_project

def test_delete_project(client, test_user, test_researcher, test_project, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/projeto/{test_project.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Project).filter(models.Project.deleted == False)) == []
