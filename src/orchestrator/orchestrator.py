from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from src.agents.ingestion.ingestion_agent import Finding
from src.agents.remediation import RemediationAgent
from src.agents.reporting import ReportingAgent
from src.agents.triage import TriageAgent

from . import Orchestrator

app = FastAPI(title="Orchestrator API")


class WorkflowRequest(BaseModel):
    start_date: str | None = None
    end_date: str | None = None


class FindingsResponse(BaseModel):
    findings: List[dict]


class TriageResult(BaseModel):
    risk_score: int


@app.get("/run")
def run_workflow(start_date: str | None = None, end_date: str | None = None):
    """Execute the orchestration workflow and return the result."""
    orch = Orchestrator(config={})
    return orch.run_workflow(start_date, end_date)


@app.post("/api/ingest", response_model=FindingsResponse)
def ingest(payload: WorkflowRequest):
    """Run the workflow and return only the findings result."""
    start_date = payload.start_date
    end_date = payload.end_date
    orch = Orchestrator(config={})
    result = orch.run_workflow(start_date, end_date)
    return {"findings": result["findings"]}


@app.post("/api/triage", response_model=TriageResult)
def triage(payload: Finding):
    """Return a triaged finding using the TriageAgent."""
    agent = TriageAgent(config={})
    return agent.triage(payload.model_dump())


class RemediationRequest(BaseModel):
    vuln_id: str


@app.post("/api/remediate")
def remediate(payload: RemediationRequest):
    """Create a remediation ticket using the RemediationAgent."""
    agent = RemediationAgent(config={})
    return agent.remediate(payload.model_dump())


@app.get("/api/report")
def report() -> dict:
    """Generate a simple report using the ReportingAgent."""
    agent = ReportingAgent(config={})
    return agent.report([])
