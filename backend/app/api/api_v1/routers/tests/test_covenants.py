#!/usr/bin/env python3

from app.db import models

def test_edit_covenant(client, test_user, test_covenant, user_token_headers):
    new_covenant = {
        "name": "Covenant 2",
        "initials": "CCT",
    }
    response = client.put(
        f"api/v1/convenio/{test_covenant.id}",
        json=new_covenant,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_covenant['id'] = test_covenant.id
    new_covenant['owner_id'] = test_covenant.owner_id
    new_covenant['logo_file'] = test_covenant.logo_file
    assert response.json() == new_covenant

def test_delete_covenant(client, test_user, test_covenant, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/convenio/{test_covenant.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Covenant).filter(models.Covenant.deleted == False)) == []
