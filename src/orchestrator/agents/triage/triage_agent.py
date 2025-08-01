from src.templates import BaseAgent


class TriageAgent(BaseAgent):
    """Assigns risk scores using Azure OpenAI."""

    def triage(self, finding: dict) -> dict:
        """Return finding with a dummy risk score."""
        score = len(str(finding)) % 5
        result = dict(finding)
        result["risk_score"] = score
        return result
