#!/usr/bin/env python3

from app.db import models

import pathlib
from io import StringIO

def test_add_covenant(client, test_user, user_token_headers):
    new_covenant = {
        "name": "Covenant 2",
        "initials": "CCT",
        "object": "Object",
    }
    path = f"{pathlib.Path(__file__).parent.absolute()}/test_files/test_logo.jpg"
    _files = {'logo_file': open(path, 'rb')}
    response = client.post(
        f"api/v1/convenio",
        data=new_covenant,
        files=_files,
        headers=user_token_headers,
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_covenant.items())

def test_edit_covenant(client, test_user, test_covenant, user_token_headers):
    new_covenant = {
        "name": "Covenant 2",
        "initials": "CCT",
        "finished": True,
        "object": "Object 3",
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
