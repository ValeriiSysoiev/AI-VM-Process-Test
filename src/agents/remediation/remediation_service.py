from fastapi import FastAPI
from . import RemediationAgent

app = FastAPI(title="Remediation Agent API")


@app.post("/api/remediate")
def remediate_endpoint(payload: dict) -> dict:
    """Create a remediation ticket."""
    agent = RemediationAgent(config={})
    return agent.remediate(payload)
