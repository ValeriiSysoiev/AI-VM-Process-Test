from src.agents.triage import TriageAgent


def test_triage_returns_risk_score():
    agent = TriageAgent(config={})
    result = agent.triage({"id": 1})
    assert isinstance(result, dict)
    assert "risk_score" in result
