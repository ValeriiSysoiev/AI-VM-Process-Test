from fastapi import FastAPI
from . import TriageAgent

app = FastAPI(title="Triage Agent API")

@app.post("/api/triage")
def triage_endpoint(finding: dict) -> dict:
    """Return a triaged finding."""
    agent = TriageAgent(config={})
    return agent.triage(finding)
