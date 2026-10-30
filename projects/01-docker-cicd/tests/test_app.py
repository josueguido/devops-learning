from unittest.mock import patch

import app
import psycopg


def test_health_reports_database_connection():
    client = app.create_app().test_client()

    with patch("db.check_connection") as check_connection:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok", "database": "ok"}
    check_connection.assert_called_once_with()


def test_health_reports_database_failure(caplog):
    client = app.create_app().test_client()

    with patch("db.check_connection", side_effect=psycopg.OperationalError("offline")):
        response = client.get("/api/health")

    assert response.status_code == 503
    assert response.json == {"status": "unavailable", "database": "unavailable"}
    assert "Database health check failed" in caplog.text


def test_get_tasks_returns_database_rows():
    tasks = [{"id": 1, "title": "Deploy", "completed": False}]
    client = app.create_app().test_client()

    with patch("db.list_tasks", return_value=tasks):
        response = client.get("/api/tasks")

    assert response.status_code == 200
    assert response.json == tasks


def test_post_task_trims_title_and_returns_created_task():
    task = {"id": 2, "title": "Practice CI", "completed": False}
    client = app.create_app().test_client()

    with patch("db.create_task", return_value=task) as create_task:
        response = client.post("/api/tasks", json={"title": "  Practice CI  "})

    assert response.status_code == 201
    assert response.json == task
    create_task.assert_called_once_with("Practice CI")


def test_post_task_rejects_empty_title():
    client = app.create_app().test_client()

    with patch("db.create_task") as create_task:
        response = client.post("/api/tasks", json={"title": "   "})

    assert response.status_code == 400
    create_task.assert_not_called()


def test_post_task_rejects_title_over_120_characters():
    client = app.create_app().test_client()

    with patch("db.create_task") as create_task:
        response = client.post("/api/tasks", json={"title": "a" * 121})

    assert response.status_code == 400
    create_task.assert_not_called()
