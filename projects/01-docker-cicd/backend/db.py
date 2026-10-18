import os

import psycopg
from psycopg.rows import dict_row


def get_connection():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL must be set")
    return psycopg.connect(database_url, row_factory=dict_row)


def check_connection():
    with get_connection() as connection:
        connection.execute("SELECT 1")


def list_tasks():
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT id, title, completed, created_at
            FROM tasks
            ORDER BY id
            """
        ).fetchall()
    return rows


def create_task(title):
    with get_connection() as connection:
        row = connection.execute(
            """
            INSERT INTO tasks (title)
            VALUES (%s)
            RETURNING id, title, completed, created_at
            """,
            (title,),
        ).fetchone()
    return row
