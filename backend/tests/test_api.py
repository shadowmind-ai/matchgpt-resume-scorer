import sys
import os

# Add the backend/app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app.main import app


from fastapi.testclient import TestClient

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_score_valid_input():
    payload = {
        "resume": "Experienced Python developer with 5+ years of backend work.",
        "job_description": "We are hiring a backend Python engineer."
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 200
    assert "match_score" in response.json()
    assert 0.0 <= response.json()["match_score"] <= 1.0

def test_score_empty_input():
    payload = {
        "resume": "",
        "job_description": ""
    }
    response = client.post("/score", json=payload)
    assert response.status_code == 422
