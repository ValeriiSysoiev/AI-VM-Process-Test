try:
    from src.templates import BaseAgent
except ModuleNotFoundError:  # allow running standalone
    from templates import BaseAgent


class ReportingAgent(BaseAgent):
    """Generates reports and dashboards."""

    def report(self, data):
        """Return a simple summary report."""
        return {"total_items": len(data)}
