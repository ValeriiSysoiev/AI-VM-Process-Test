from typing import List, Optional

import httpx
import logging
import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
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
        json_schema_extra={"example": "Nexpose"},
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


@app.get("/", tags=["health"])
def healthcheck() -> dict:
    """Basic healthcheck endpoint."""
    return {"status": "ok"}


# Example finding returned by the endpoint
EXAMPLE_FINDING = {
    "vuln_id": "CVE-2025-12345",
    "scanner": "Nexpose",
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


def _parse_assets(data: dict) -> List[Finding]:
    """Convert Nexpose asset data into ``Finding`` records.

    Because the Nexpose API returns a large JSON structure, this helper pulls
    a minimal set of fields to populate the ``Finding`` model. Any missing
    values fall back to sensible defaults so the ingestion agent can operate
    even if certain keys are unavailable.
    """

    findings: List[Finding] = []
    for asset in data.get("resources", []):
        vuln_id = str(asset.get("id", "unknown"))
        enrichment = Enrichment(
            asset_owner=str(asset.get("owner", "unknown")),
            business_criticality=str(asset.get("importance", "Unknown")),
        )
        finding = Finding(
            vuln_id=vuln_id,
            scanner="Nexpose",
            asset_id=str(asset.get("id", "unknown")),
            risk_rating=str(asset.get("riskScore", "Unknown")),
            description=str(asset.get("host-name", asset.get("ip", "Nexpose asset"))),
            date_detected=str(
                asset.get("lastScanTime", asset.get("last_assessed_for_vulnerabilities", ""))
            ),
            enrichment=enrichment,
            risk_score=int(asset.get("riskScore", 0)),
            status="Pending",
        )
        findings.append(finding)
    return findings


def _get_secret(secret_name: str) -> Optional[str]:
    """Retrieve a secret from Azure Key Vault."""
    vault_name = os.getenv("KEY_VAULT_NAME")
    if not vault_name:
        logging.warning("KEY_VAULT_NAME not set; skipping Nexpose API call")
        return None

    try:
        credential = DefaultAzureCredential()
        client = SecretClient(
            vault_url=f"https://{vault_name}.vault.azure.net",
            credential=credential,
        )
        return client.get_secret(secret_name).value
    except Exception as exc:  # noqa: BLE001
        logging.error("Failed to retrieve secret %s: %s", secret_name, exc)
        return None


async def fetch_nexpose_assets() -> Optional[dict]:
    """Fetch asset information from the Nexpose API."""
    api_url = _get_secret("nexpose-api-url")
    user = _get_secret("nexpose-user")
    password = _get_secret("nexpose-password")

    if not all([api_url, user, password]):
        return None

    url = f"{api_url.rstrip('/')}/api/3/assets"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, auth=(user, password), timeout=10)
            response.raise_for_status()
            logging.info("Nexpose assets response snippet: %s", response.text[:200])
            return response.json()
    except Exception as exc:  # noqa: BLE001
        logging.error("Error calling Nexpose API: %s", exc)
        return None


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

    data = await fetch_nexpose_assets()
    if data:
        parsed = _parse_assets(data)
        if parsed:
            return parsed
    return [Finding(**EXAMPLE_FINDING)]
