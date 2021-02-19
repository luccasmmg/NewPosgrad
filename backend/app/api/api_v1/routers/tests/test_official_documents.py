#!/usr/bin/env python3

from app.db import models

def test_edit_official_document(client, test_user, test_official_document, user_token_headers):
    new_official_document = {
        "title": "Official Document 2",
        "cod": "CCT",
        "category": "others",
    }
    response = client.put(
        f"api/v1/documento/{test_official_document.id}",
        json=new_official_document,
        headers=user_token_headers
    )
    assert response.status_code == 200
    new_official_document['id'] = test_official_document.id
    new_official_document['owner_id'] = test_official_document.owner_id
    response = {i:response.json()[i] for i in response.json() if i!='inserted_on'}
    assert response == new_official_document

def test_delete_official_document(client, test_user, test_official_document, user_token_headers, test_db):
    response = client.delete(
        f"api/v1/documento/{test_official_document.id}",
        headers=user_token_headers
    )
    assert response.status_code == 200
    assert list(test_db.query(models.OfficialDocument).filter(models.OfficialDocument.deleted == False)) == []
