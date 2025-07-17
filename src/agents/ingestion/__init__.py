from src.templates import BaseAgent

from .ingestion_agent import EXAMPLE_FINDING


class IngestionAgent(BaseAgent):
    """Fetches vulnerabilities from scanners."""

    def ingest(self, start_date, end_date):
        """Return example vulnerability findings."""
        return [dict(EXAMPLE_FINDING)]
