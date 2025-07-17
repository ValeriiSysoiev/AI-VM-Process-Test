# Deployment Scripts

This folder contains sample steps for deploying the infrastructure Bicep templates located in [`../../05_Infrastructure/`](../../05_Infrastructure/).

## Prerequisites
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) with Bicep support
- An Azure subscription and resource group (`az group create -n <rg> -l <region>`)
- Logged in via `az login`

## Example deployment script
Create a `deploy.sh` script and adjust the parameter values to match your environment:

```bash
#!/usr/bin/env bash
set -e

RESOURCE_GROUP="<rg>"
LOCATION="<region>"

az deployment group create \
  --resource-group "$RESOURCE_GROUP" \
  --template-file ../../05_Infrastructure/main.bicep \
  --parameters containerEnvName="vm-env" \
               orchestratorAppName="vm-orchestrator" \
               ingestionAppName="vm-ingestion" \
               frontendAppName="vm-frontend" \
               triageAppName="vm-triage" \
               remediationAppName="vm-remediation" \
               reportingAppName="vm-reporting" \
               cosmosAccountName="vm-cosmos" \
               keyVaultName="vm-kv" \
               openAiAccountName="vm-openai"
```

Run the script:

```bash
chmod +x deploy.sh
./deploy.sh
```

The `main.bicep` file orchestrates modules for container apps, Cosmos DB, Key Vault and Azure OpenAI. Adjust parameter names if you customize the templates.

## Cleanup

Remove the resource group when finished:

```bash
az group delete --name <rg> --yes --no-wait
```
