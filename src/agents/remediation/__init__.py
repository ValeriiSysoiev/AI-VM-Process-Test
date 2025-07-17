from src.templates import BaseAgent


class RemediationAgent(BaseAgent):
    """Creates tickets in ITSM platforms."""

    def remediate(self, finding: dict):
        """Return a dummy ticket for the finding."""
        ticket_id = f"TICKET-{finding.get('vuln_id', '0')}"
        return {"ticket_id": ticket_id, "status": "created"}
