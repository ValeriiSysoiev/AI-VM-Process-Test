from src.agents.approval import ApprovalAgent


def test_review_marks_approved():
    agent = ApprovalAgent(config={})
    items = [{"vuln_id": "CVE-1"}]
    result = agent.review(items)
    assert isinstance(result, list)
    assert result[0]["approved"] is True
