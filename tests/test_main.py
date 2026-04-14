from fastapi.testclient import TestClient

from app.main import app


def test_health_returns_message() -> None:
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello, FastAPI with uv!"}


def test_unknown_path_is_404() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 404
