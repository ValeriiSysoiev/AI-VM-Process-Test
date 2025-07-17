from src.templates import BaseAgent


class EnrichmentAgent(BaseAgent):
    """Add context to findings."""

    def enrich(self, findings: list[dict]) -> list[dict]:
        enriched = []
        for finding in findings:
            result = dict(finding)
            result.setdefault("enrichment", {})
            result["enrichment"].update({"context": "example"})
            enriched.append(result)
        return enriched
