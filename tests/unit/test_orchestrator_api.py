from fastapi.testclient import TestClient

from src.orchestrator.orchestrator import app
from src.agents.ingestion.ingestion_agent import EXAMPLE_FINDING


def test_orchestrator_ingest_returns_findings():
    client = TestClient(app)
    response = client.post(
        "/api/ingest",
        json={"start_date": "2025-07-01", "end_date": "2025-07-07"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "findings" in data
    assert isinstance(data["findings"], list)
    assert len(data["findings"]) > 0


def test_run_returns_findings():
    """Ensure the /run endpoint returns workflow results."""
    client = TestClient(app)
    response = client.get(
        "/run",
        params={"start_date": "2025-07-01", "end_date": "2025-07-07"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["findings"] and "vuln_id" in data["findings"][0]


def test_triage_endpoint_returns_score():
    client = TestClient(app)
    response = client.post("/api/triage", json=EXAMPLE_FINDING)
    assert response.status_code == 200
    data = response.json()
    assert "risk_score" in data


def test_ingest_invalid_payload_returns_200():
    """Extra fields are ignored so the endpoint should still return 200."""
    client = TestClient(app)
    response = client.post("/api/ingest", json={"foo": "bar"})
    assert response.status_code == 200


def test_triage_invalid_payload_returns_422():
    client = TestClient(app)
    response = client.post("/api/triage", json={"foo": "bar"})
    assert response.status_code == 422


def test_remediate_endpoint_returns_ticket():
    client = TestClient(app)
    response = client.post("/api/remediate", json={"vuln_id": "CVE-1"})
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "created"


def test_report_endpoint_returns_summary():
    client = TestClient(app)
    response = client.get("/api/report")
    assert response.status_code == 200
    data = response.json()
    assert "total_items" in data
