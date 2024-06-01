# tests/test_app.py
from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_process_data_success():
    request_payload = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/process", json=request_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"

def test_process_data_invalid_payload():
    request_payload = {
        "batchid": "id0101",
        "payload": "invalid_payload"
    }
    response = client.post("/process", json=request_payload)
    assert response.status_code == 422  # Unprocessable Entity for validation error
