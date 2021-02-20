#!/usr/bin/env python3

from app.db import models

def test_add_event_no_url(client, test_user, user_token_headers):
    new_event = {
        "title": "string",
        "link": "string",
        "initial_date": "2021-02-20T15:31:19.739000+00:00",
        "final_date": "2021-02-20T15:31:19.739000+00:00"
    }
    response = client.post(
        f"api/v1/evento",
        json=new_event,
        headers=user_token_headers
    )
    assert response.status_code == 422

def test_add_event(client, test_user, user_token_headers):
    new_event = {
        "title": "string",
        "link": "https://google.com",
        "initial_date": "2021-02-20T15:31:19.739000+00:00",
        "final_date": "2021-02-20T15:31:19.739000+00:00"
    }
    response = client.post(
        f"api/v1/evento",
        json=new_event,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_event['id'] = 1
    new_event['owner_id'] = test_user.owner_id
    assert response.json() == new_event

def test_edit_event(client, test_user, test_event, user_token_headers):
    new_event = {
        "title": "string 2",
        "link": "https://duckduckgo.com",
        "initial_date": "2021-02-20T15:31:19.739000+00:00",
        "final_date": "2021-02-20T15:31:19.739000+00:00"
    }
    response = client.put(
        f"api/v1/evento/{test_event.id}",
        json=new_event,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_event['id'] = test_event.id
    new_event['owner_id'] = test_event.owner_id
    assert response.json() == new_event

def test_delete_event(client, test_user, test_event, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/evento/{test_event.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Event).filter(models.Event.deleted == False)) == []
