from src.agents.ingestion import IngestionAgent


def test_ingest_returns_list():
    agent = IngestionAgent(config={})
    results = agent.ingest("2025-07-01", "2025-07-07")
    assert isinstance(results, list)
    assert results and "vuln_id" in results[0]
