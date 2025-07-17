from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Enrichment(BaseModel):
    """Additional context about an asset."""

    asset_owner: str = Field(
        ...,
        json_schema_extra={"example": "jdoe@company.com"},
    )
    business_criticality: str = Field(
        ...,
        json_schema_extra={"example": "Critical"},
    )


class Finding(BaseModel):
    """Representation of a vulnerability finding."""

    vuln_id: str = Field(
        ...,
        json_schema_extra={"example": "CVE-2025-12345"},
    )
    scanner: str = Field(
        ...,
        json_schema_extra={"example": "Qualys"},
    )
    asset_id: str = Field(
        ...,
        json_schema_extra={"example": "SRV-001"},
    )
    risk_rating: str = Field(
        ...,
        json_schema_extra={"example": "High"},
    )
    description: str = Field(
        ...,
        json_schema_extra={"example": "Buffer overflow in ..."},
    )
    date_detected: str = Field(
        ...,
        json_schema_extra={"example": "2025-07-07"},
    )
    enrichment: Enrichment
    risk_score: int = Field(
        ...,
        json_schema_extra={"example": 85},
    )
    status: str = Field(
        ...,
        json_schema_extra={"example": "Pending"},
    )


app = FastAPI(title="Ingestion Agent API")

# Example finding returned by the endpoint
EXAMPLE_FINDING = {
    "vuln_id": "CVE-2025-12345",
    "scanner": "Qualys",
    "asset_id": "SRV-001",
    "risk_rating": "High",
    "description": "Buffer overflow in ...",
    "date_detected": "2025-07-07",
    "enrichment": {
        "asset_owner": "jdoe@company.com",
        "business_criticality": "Critical",
    },
    "risk_score": 85,
    "status": "Pending",
}


@app.post(
    "/api/ingest",
    response_model=List[Finding],
    summary="Ingest vulnerability findings",
    tags=["ingestion"],
)
async def ingest_finding(finding: Finding) -> List[Finding]:
    """Accept a vulnerability finding and return a sample list.

    This endpoint validates the incoming finding against the ``Finding`` schema
    and returns a static example list demonstrating what an ingestion
    agent might return.
    """

    return [Finding(**EXAMPLE_FINDING)]
