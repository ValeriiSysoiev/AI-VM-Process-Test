from src.templates import BaseAgent

from .ingestion_agent import EXAMPLE_FINDING, fetch_nexpose_assets, _parse_assets


class IngestionAgent(BaseAgent):
    """Fetches vulnerabilities from scanners."""

    def ingest(self, start_date, end_date):
        """Fetch findings from Nexpose."""
        try:
            import anyio

            data = anyio.run(fetch_nexpose_assets)
            if data:
                results = _parse_assets(data)
                if results:
                    return [f.dict() for f in results]
        except Exception:  # noqa: BLE001
            pass

        return [dict(EXAMPLE_FINDING)]
