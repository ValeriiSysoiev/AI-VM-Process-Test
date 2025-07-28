from src.templates import BaseAgent

from .ingestion_agent import EXAMPLE_FINDING, fetch_nexpose_assets


class IngestionAgent(BaseAgent):
    """Fetches vulnerabilities from scanners."""

    def ingest(self, start_date, end_date):
        """Fetch findings from Nexpose and return example data."""
        # For demonstration, we trigger a Nexpose API call and ignore the result.
        # The actual findings returned to callers remain static.
        try:
            import anyio

            anyio.run(fetch_nexpose_assets)
        except Exception:  # noqa: BLE001
            pass

        return [dict(EXAMPLE_FINDING)]
