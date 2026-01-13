import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/current", params={"city", "Paris"})
    assert response.status_code == 200

    response = client.get("/api/current", params={"city", "azertyuiop"})
    assert response.status_code == 404
