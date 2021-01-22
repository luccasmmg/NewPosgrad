#!/usr/bin/env python3

from app.db import models

def test_create_course(client, test_superuser, superuser_token_headers):
    new_course = {
        "owner_id": test_superuser.owner_id,
        "name": "Música 2",
        "id_sigaa": 284,
        "course_type":models.CourseType.masters
    }
    response = client.post(
        f"api/v1/curso",
        json=new_course,
        headers=superuser_token_headers
    )
    assert response.status_code == 200
    assert all(item in response.json().items() for item in new_course.items())
