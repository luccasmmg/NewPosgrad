#!/usr/bin/env python3

from app.db import models
from app.schemas import pg_information_schemas
from app.schemas import base_schemas

def test_get_researchers(client, test_db, test_pg, test_researcher):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/pesquisadores")
    assert response.status_code == 200
    assert response.json()[0] == dict(pg_information_schemas.Researcher.from_orm(test_researcher))

def test_get_covenant(client, test_db, test_pg, test_covenant):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/convenios")
    assert response.status_code == 200
    assert response.json()[0] == dict(pg_information_schemas.Covenant.from_orm(test_covenant))

def test_get_participation(client, test_db, test_pg, test_participation):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/participacoes")
    assert response.status_code == 200
    assert response.json()[0] == dict(pg_information_schemas.Participation.from_orm(test_participation))

def test_get_pg(client, test_db, test_pg, test_attendance):
    response = client.get(f"/api/v1/publico/{test_pg.initials}")
    assert response.status_code == 200
    assert response.json() == dict(base_schemas.PostGraduation.from_orm(test_pg))
