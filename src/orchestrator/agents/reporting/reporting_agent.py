from src.templates import BaseAgent


class ReportingAgent(BaseAgent):
    """Generates reports and dashboards."""

    def report(self, data) -> dict:
        """Return a simple summary report."""
        return {"total_items": len(data)}
