import logging

import db
import psycopg
from flask import Flask, jsonify, request
from flask_cors import CORS

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost"}})

    @app.get("/api/health")
    def health():
        try:
            db.check_connection()
        except (psycopg.Error, RuntimeError):
            logger.exception("Database health check failed")
            return jsonify({"status": "unavailable", "database": "unavailable"}), 503
        return jsonify({"status": "ok", "database": "ok"})

    @app.get("/api/tasks")
    def get_tasks():
        try:
            tasks = db.list_tasks()
        except (psycopg.Error, RuntimeError):
            logger.exception("Could not list tasks")
            return jsonify({"error": "Database unavailable"}), 503
        return jsonify(tasks)

    @app.post("/api/tasks")
    def post_task():
        payload = request.get_json(silent=True)
        title = payload.get("title") if isinstance(payload, dict) else None
        if not isinstance(title, str) or not title.strip() or len(title.strip()) > 120:
            return jsonify({"error": "title must contain between 1 and 120 characters"}), 400

        try:
            task = db.create_task(title.strip())
        except (psycopg.Error, RuntimeError):
            logger.exception("Could not create task")
            return jsonify({"error": "Database unavailable"}), 503
        return jsonify(task), 201

    return app


app = create_app()
