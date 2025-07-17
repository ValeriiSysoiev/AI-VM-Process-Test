from src.agents.reporting import ReportingAgent


def test_report_returns_dict():
    agent = ReportingAgent(config={})
    result = agent.report([])
    assert isinstance(result, dict)
