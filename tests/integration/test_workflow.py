from src.orchestrator import Orchestrator
from src.agents.ingestion.ingestion_agent import EXAMPLE_FINDING


def test_workflow_runs():
    orch = Orchestrator(config={})
    assert hasattr(orch, "run_workflow")


def test_workflow_executes_stub_agents():
    orch = Orchestrator(config={})
    result = orch.run_workflow("2025-07-01", "2025-07-07")
    assert set(result.keys()) == {
        "findings",
        "deduplicated",
        "enriched",
        "triaged",
        "approved",
        "tickets",
        "report",
    }
    assert result["tickets"][0]["ticket_id"] == f"TICKET-{EXAMPLE_FINDING['vuln_id']}"
