from src.agents.deduplication import DeduplicationAgent


def test_deduplicate_removes_duplicates():
    agent = DeduplicationAgent(config={})
    findings = [
        {"vuln_id": "CVE-1"},
        {"vuln_id": "CVE-1"},
        {"vuln_id": "CVE-2"},
    ]
    result = agent.deduplicate(findings)
    assert isinstance(result, list)
    assert len(result) == 2
