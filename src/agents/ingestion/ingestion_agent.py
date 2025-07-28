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
    """Fetch a sample asset list from Nexpose."""
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

    await fetch_nexpose_assets()
    return [Finding(**EXAMPLE_FINDING)]
