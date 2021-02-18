#!/usr/bin/env python3

#!/usr/bin/env python3

from app.db import models

def test_edit_attendance(client, test_pg, test_superuser, test_attendance, superuser_token_headers):
    new_attendance = {
        "email": "email2@gmail.com",
        "location": "Location test",
        "schedule": "Schedule test",
    }
    response = client.put(
        f"api/v1/contato",
        json=new_attendance,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    new_attendance["id"] = test_attendance.id
    new_attendance["owner_id"] = test_attendance.owner_id
    new_attendance["phones"] = []
    assert response.json() == new_attendance

def test_create_attendance(client, test_superuser, superuser_token_headers):
    new_attendance = {
        "owner_id": test_superuser.owner_id,
        "email": "email2@gmail.com",
        "location": "Location test",
        "schedule": "Schedule test",
    }
    response = client.post(
        f"api/v1/contato",
        json=new_attendance,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_attendance.items())
