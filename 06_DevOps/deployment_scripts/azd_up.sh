#!/usr/bin/env bash
set -euo pipefail

# Run azd up with parameters loaded from .env if available
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

ENV_NAME="${ENV_NAME:-vm-env}"
LOCATION="${LOCATION:-eastus}"
SUBSCRIPTION="${AZURE_SUBSCRIPTION_ID:-}"

ORCH_IMG="${ORCHESTRATOR_IMAGE:-mcr.microsoft.com/azuredocs/containerapps-helloworld:latest}"
INGEST_IMG="${INGESTION_IMAGE:-mcr.microsoft.com/azuredocs/containerapps-helloworld:latest}"

ARGS=(--environment "$ENV_NAME" --location "$LOCATION")
if [ -n "$SUBSCRIPTION" ]; then
  ARGS+=(--subscription "$SUBSCRIPTION")
fi

azd up "${ARGS[@]}" \
  --infra-parameter orchestratorImage="$ORCH_IMG" \
  --infra-parameter ingestionImage="$INGEST_IMG" \
  --infra-parameter minReplicas=1 \
  --infra-parameter maxReplicas=1 \
  --infra-parameter cpu='0.5' \
  --infra-parameter memory=1Gi

