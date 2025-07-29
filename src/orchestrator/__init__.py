import logging

from src.agents.approval import ApprovalAgent
from src.agents.deduplication import DeduplicationAgent
from src.agents.enrichment import EnrichmentAgent
from src.agents.ingestion import IngestionAgent
from src.agents.remediation import RemediationAgent
from src.agents.reporting import ReportingAgent
from src.agents.triage import TriageAgent


class Orchestrator:
    """Coordinates the vulnerability management workflow."""

    def __init__(self, config: dict):
        self.config = config
        self.log = logging.getLogger(self.__class__.__name__)

    def run_workflow(self, start_date=None, end_date=None):
        """Run the stubbed orchestration workflow."""
        ingestion = IngestionAgent(self.config.get("ingestion", {}))
        dedupe = DeduplicationAgent(self.config.get("deduplication", {}))
        enrichment = EnrichmentAgent(self.config.get("enrichment", {}))
        triage = TriageAgent(self.config.get("triage", {}))
        approval = ApprovalAgent(self.config.get("approval", {}))
        remediation = RemediationAgent(self.config.get("remediation", {}))
        reporting = ReportingAgent(self.config.get("reporting", {}))

        self.log.info("Starting ingestion")
        findings = ingestion.ingest(start_date, end_date)
        self.log.info("Deduplicating findings")
        deduplicated = dedupe.deduplicate(findings)
        self.log.info("Enriching findings")
        enriched = enrichment.enrich(deduplicated)
        self.log.info("Triaging findings")
        triaged = [triage.triage(f) for f in enriched]
        self.log.info("Approving triaged results")
        approved = approval.review(triaged)
        self.log.info("Creating remediation tickets")
        tickets = [remediation.remediate(a) for a in approved]
        self.log.info("Generating report")
        report = reporting.report(tickets)

        return {
            "findings": findings,
            "deduplicated": deduplicated,
            "enriched": enriched,
            "triaged": triaged,
            "approved": approved,
            "tickets": tickets,
            "report": report,
        }


__all__ = ["Orchestrator"]
