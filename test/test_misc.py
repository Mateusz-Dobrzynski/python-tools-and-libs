from fastapi.testclient import TestClient

from src.main import app


def test_erroneous_url_returns_404():
    # GIVEN
    client = TestClient(app)

    # WHEN
    response = client.post("/user")

    # THEN
    assert response.status_code == 404
