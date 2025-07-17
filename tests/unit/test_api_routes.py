from fastapi.testclient import TestClient

from src.api import app


from src.agents.ingestion.ingestion_agent import EXAMPLE_FINDING


def test_triage_route_returns_score():
    client = TestClient(app)
    response = client.post("/api/triage", json=EXAMPLE_FINDING)
    assert response.status_code == 200
    assert "risk_score" in response.json()


def test_remediate_route_returns_ticket():
    client = TestClient(app)
    response = client.post("/api/remediate", json={"vuln_id": "CVE-1"})
    assert response.status_code == 200
    assert response.json().get("status") == "created"


def test_report_route_returns_summary():
    client = TestClient(app)
    response = client.get("/api/report")
    assert response.status_code == 200
    assert "total_items" in response.json()
