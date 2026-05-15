import pytest
from fastapi.testclient import TestClient

from src.main import app


def test_create_user_returns_username():
    # GIVEN
    client = TestClient(app)
    request_body = {"username": "alice", "password": "secret"}

    # WHEN
    response = client.post("/users", json=request_body)

    # THEN
    assert response.status_code == 200
    assert response.json() == {"username": "alice"}


@pytest.mark.skip(reason="this can be implemented later")
def test_endpoint_for_reversing_username():
    # GIVEN
    client = TestClient(app)
    request_body = {"username": "alice"}

    # WHEN
    response = client.post("/users/reverse", json=request_body)

    # THEN
    assert response.status_code == 200
    assert response.json() == {"username": "ecila"}
