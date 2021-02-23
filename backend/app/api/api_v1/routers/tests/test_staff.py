#!/usr/bin/env python3

from app.db import models

def test_edit_staff(client, test_user, test_staff, user_token_headers):
    new_staff = {
        "name": "string",
        "rank": "coordinator",
        "description": "string"
    }
    response = client.put(
        f"api/v1/equipe/{test_staff.id}",
        json=new_staff,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_staff['id'] = test_staff.id
    new_staff['owner_id'] = test_staff.owner_id
    new_staff['photo'] = test_staff.photo
    assert response.json() == new_staff

def test_delete_staff(client, test_user, test_staff, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/equipe/{test_staff.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Staff).filter(models.Staff.deleted == False)) == []
