from fastapi.testclient import TestClient

from src.agents.ingestion.ingestion_agent import EXAMPLE_FINDING, app


def test_ingest_endpoint_returns_example():
    client = TestClient(app)
    response = client.post("/api/ingest", json=EXAMPLE_FINDING)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data and data[0]["vuln_id"] == EXAMPLE_FINDING["vuln_id"]
