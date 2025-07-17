from src.templates import BaseAgent


class ApprovalAgent(BaseAgent):
    """Simulate human approval."""

    def review(self, findings: list[dict]) -> list[dict]:
        approved = []
        for finding in findings:
            result = dict(finding)
            result["approved"] = True
            approved.append(result)
        return approved
