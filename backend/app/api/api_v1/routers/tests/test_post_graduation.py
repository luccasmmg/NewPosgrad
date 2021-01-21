#!/usr/bin/env python3

from app.db import models

def test_get_pg(client, test_pg, test_superuser):
    response = client.get("/api/v1/posgraduacao/ppgp")
    assert response.status_code == 200
    assert response.json() == {
        "id_unit": test_pg.id_unit,
        "name": test_pg.name,
        "initials": test_pg.initials,
        "sigaa_code": test_pg.sigaa_code,
        "is_signed_in": test_pg.is_signed_in,
        "old_url": test_pg.old_url,
        "description_small": test_pg.description_small,
        "description_big": test_pg.description_big,
        "id": test_pg.id,
        "users": [
            {
            "email": test_superuser.email,
            "owner_id": test_pg.id,
            "is_active": test_superuser.is_active,
            "is_superuser": test_superuser.is_superuser,
            "id": test_superuser.id
            }
        ],
        "courses": []
    }

def test_create_pg(client, test_superuser, superuser_token_headers):
    new_pg = {
        "id_unit": 1,
        "name": "Teste",
        "initials": "T",
        "sigaa_code": 1
    }
    response = client.post(
        f"/api/v1/posgraduacao",
        json=new_pg,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_pg.items())

def test_edit_pg(client, test_pg, test_superuser, superuser_token_headers):
    new_pg = {
        "id_unit": test_pg.id,
        "name": "string",
        "initials": test_pg.initials,
        "sigaa_code": test_pg.sigaa_code
    }
    response = client.put(
        f"/api/v1/posgraduacao/{test_pg.initials}",
        json=new_pg,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert response.json() == {
        "id_unit": test_pg.id_unit,
        "name": "string",
        "initials": test_pg.initials,
        "sigaa_code": test_pg.sigaa_code,
        "is_signed_in": test_pg.is_signed_in,
        "old_url": test_pg.old_url,
        "description_small": test_pg.description_small,
        "description_big": test_pg.description_big,
        "id": test_pg.id,
        "users": [
            {
            "email": test_superuser.email,
            "owner_id": test_pg.id,
            "is_active": test_superuser.is_active,
            "is_superuser": test_superuser.is_superuser,
            "id": test_superuser.id
            }
        ],
        "courses": []
    }
