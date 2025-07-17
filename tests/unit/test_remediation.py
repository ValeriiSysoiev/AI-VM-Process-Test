from src.agents.remediation import RemediationAgent


def test_remediate_returns_ticket():
    agent = RemediationAgent(config={})
    result = agent.remediate({"vuln_id": "1"})
    assert isinstance(result, dict)
    assert result.get("ticket_id") == "TICKET-1"
    assert result.get("status") == "created"
