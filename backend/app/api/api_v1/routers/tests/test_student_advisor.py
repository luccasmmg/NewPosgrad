#!/usr/bin/env python3

from app.db import models

def test_add_student_advisor(client, test_user, user_token_headers):
    new_student_advisor = {
        "advisor_name": "Maria Arlete",
        "registration": 11111111111,
    }
    response = client.post(
        f"api/v1/coordenador",
        json=new_student_advisor,
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_student_advisor.items())

def test_edit_student_advisor(client, test_user, test_student_advisor, user_token_headers):
    new_student_advisor = {
        "advisor_name": "Marconi Neves Macedo",
        "registration": 11111111111,
    }
    response = client.put(
        f"api/v1/coordenador/{test_student_advisor.id}",
        json=new_student_advisor,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_student_advisor['id'] = test_student_advisor.id
    new_student_advisor['owner_id'] = test_student_advisor.owner_id
    assert response.json() == new_student_advisor

def test_delete_student_advisor(client, test_user, test_student_advisor, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/coordenador/{test_student_advisor.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.StudentAdvisor).filter(models.StudentAdvisor.deleted == False)) == []
