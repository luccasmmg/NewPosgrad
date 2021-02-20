#!/usr/bin/env python3

from app.db import models

def test_add_news(client, test_user, user_token_headers):
    new_news = {
        "title": "string",
        "headline": "string",
        "date": "2021-02-20",
        "body": "string"
    }
    response = client.post(
        f"api/v1/noticia",
        json=new_news,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_news['id'] = 1
    new_news['owner_id'] = test_user.owner_id
    assert response.json() == new_news

def test_edit_news(client, test_user, test_news, user_token_headers):
    new_news = {
        "title": "string 2",
        "headline": "string 2",
        "date": "2021-02-21",
        "body": "string 2"
    }
    response = client.put(
        f"api/v1/noticia/{test_news.id}",
        json=new_news,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_news['id'] = test_news.id
    new_news['owner_id'] = test_news.owner_id
    assert response.json() == new_news

def test_delete_news(client, test_user, test_news, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/noticia/{test_news.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.Event).filter(models.Event.deleted == False)) == []
