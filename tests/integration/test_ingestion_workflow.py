import pytest
from fastapi.testclient import TestClient

from src.api import app


@pytest.mark.integration
def test_ingest_endpoint_returns_findings():
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
