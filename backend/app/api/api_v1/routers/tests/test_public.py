#!/usr/bin/env python3

from app.db import models
from app.schemas import pg_information_schemas
from app.schemas import base_schemas

def test_get_researchers(client, test_db, test_pg, test_researcher):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/pesquisadores")
    assert response.status_code == 200

def test_get_covenant(client, test_db, test_pg, test_covenant):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/convenios")
    assert response.status_code == 200

def test_get_participation(client, test_db, test_pg, test_participation):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/participacoes")
    assert response.status_code == 200

def test_get_official_documents(client, test_db, test_pg, test_official_document):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/documentos")
    assert response.status_code == 200

def test_get_news(client, test_db, test_pg, test_news):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/noticias")
    assert response.status_code == 200

def test_get_events(client, test_db, test_pg, test_event):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/eventos")
    assert response.status_code == 200

def test_get_staff(client, test_db, test_pg, test_staff):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/equipe")
    assert response.status_code == 200

def test_get_scheduled_report(client, test_db, test_pg, test_scheduled_report):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/defesas")
    assert response.status_code == 200

def test_get_student_advisors(client, test_db, test_pg, test_student_advisor):
    response = client.get(f"/api/v1/publico/{test_pg.initials}/orientadores")
    assert response.status_code == 200

def test_get_pg(client, test_db, test_pg, test_attendance):
    response = client.get(f"/api/v1/publico/{test_pg.initials}")
    assert response.status_code == 200
