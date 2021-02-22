#!/usr/bin/env python3

from app.db import models

def test_add_scheduled_report(client, test_user, user_token_headers):
    new_scheduled_report = {
        "title": "string",
        "author": "string",
        "location": "string",
        "datetime": "2021-02-20T15:31:19.739000+00:00"
    }
    response = client.post(
        f"api/v1/defesa",
        json=new_scheduled_report,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_scheduled_report['id'] = 1
    new_scheduled_report['owner_id'] = test_user.owner_id
    assert response.json() == new_scheduled_report

def test_edit_scheduled_report(client, test_user, test_scheduled_report, user_token_headers):
    new_scheduled_report = {
        "title": "string",
        "author": "string",
        "location": "string",
        "datetime": "2021-02-20T15:31:19.739000+00:00"
    }
    response = client.put(
        f"api/v1/defesa/{test_scheduled_report.id}",
        json=new_scheduled_report,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_scheduled_report['id'] = test_scheduled_report.id
    new_scheduled_report['owner_id'] = test_scheduled_report.owner_id
    assert response.json() == new_scheduled_report

def test_delete_scheduled_report(client, test_user, test_scheduled_report, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/defesa/{test_scheduled_report.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.ScheduledReport).filter(models.ScheduledReport.deleted == False)) == []
