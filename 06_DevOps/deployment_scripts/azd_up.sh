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

USE_SAMPLE_IMAGES="${USE_SAMPLE_IMAGES:-}"
if [ -z "$USE_SAMPLE_IMAGES" ]; then
  if [[ "${ENV_NAME,,}" =~ prod ]]; then
    USE_SAMPLE_IMAGES="false"
  else
    USE_SAMPLE_IMAGES="true"
  fi
fi

ARGS=(--environment "$ENV_NAME" --location "$LOCATION")
if [ -n "$SUBSCRIPTION" ]; then
  ARGS+=(--subscription "$SUBSCRIPTION")
fi

azd up "${ARGS[@]}" \
  --infra-parameter useSampleImages="$USE_SAMPLE_IMAGES" \
  --infra-parameter minReplicas=1 \
  --infra-parameter maxReplicas=1 \
  --infra-parameter cpu='0.5' \
  --infra-parameter memory=1Gi

