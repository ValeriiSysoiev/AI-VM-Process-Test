from fastapi import FastAPI
from src.agents.reporting.reporting_agent import ReportingAgent

app = FastAPI(title="Reporting Agent API")


@app.get("/api/report")
def report_endpoint() -> dict:
    """Return a simple report."""
    agent = ReportingAgent(config={})
    return agent.report([])
