# Frontend Orchestrator UI

This web interface comes from the Microsoft solution accelerator and now serves as the user portal for the Vulnerability Management orchestrator.

## Workflow Stages
1. Ingestion
2. Deduplication
3. Enrichment
4. Triage
5. Approval
6. Remediation
7. Reporting

## Supported Agent Roles
- `IngestionAgent`
- `DeduplicationAgent`
- `EnrichmentAgent`
- `TriageAgent`
- `ApprovalAgent`
- `RemediationAgent`
- `ReportingAgent`

## Execute frontend UI App
```shell
uv run uvicorn frontend_server:app --port 3000
```
The server binds to `127.0.0.1:3000` by default. Set the `FRONTEND_HOST`
and `FRONTEND_PORT` environment variables to override the listen address.

## Running Jest Tests

Install the Node dependencies and execute the test suite which automatically starts `frontend_server.py`:

```bash
npm ci
npm test
```
