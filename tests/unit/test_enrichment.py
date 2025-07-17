from src.agents.enrichment import EnrichmentAgent


def test_enrich_adds_context():
    agent = EnrichmentAgent(config={})
    findings = [{"vuln_id": "CVE-1"}]
    result = agent.enrich(findings)
    assert isinstance(result, list)
    assert result[0]["enrichment"]["context"] == "example"
