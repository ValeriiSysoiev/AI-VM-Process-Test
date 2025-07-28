**Diagram Code:**
```eraser#

// Title

title Vulnerability Management Orchestration Architecture (Clear, Grouped, Annotated), Grouped, Annotated), Grouped, Annotated), Grouped, Annotated), Grouped, Annotated), Grouped, Annotated)



// USER LAYER

User Layer [icon: user] {

Security Analyst [icon: user]

User Portal [icon: monitor, label: "Web UI"]

}



// ORCHESTRATION LAYER

Orchestration Layer [icon: robot] {

Orchestrator AI Agent [icon: robot, label: "FastAPI Orchestrator AI Agent"]

}



// INGESTION AGENTS LAYER

Ingestion Agents [color: blue, icon: robot] {

Nexpose AI Agent [icon: robot, label: "Nexpose"]

Wiz AI Agent [icon: robot, label: "Wiz"]

Defender AI Agent [icon: robot, label: "Defender"]

WebApp Scanner AI Agent [icon: robot, label: "WebApp Scanner"]

}



// PROCESSING LAYER

Processing [color: green, icon: cpu] {

Deduplication & Normalization [icon: filter, label: "Deduplication"]

Enrichment AI Agent [icon: robot, label: "Enrichment (AI Agent)"]

Triage & Risk Scoring AI Agent [icon: robot, label: "Triage & Risk Scoring (LLM AI Agent)"]

}



// HUMAN REVIEW LAYER

Human Review [color: yellow, icon: user-check] {

Review & Approval [icon: user-check, label: "Human-in-the-Loop Approval"]

}



// REMEDIATION & REPORTING LAYER

Remediation & Reporting [color: orange, icon: check-circle] {

Ticketing Agent [icon: jira, label: "Remediation/Ticketing (SNOW/Jira)"]

Reporting AI Agent [icon: robot, label: "Reporting (AI Agent)"]

Dashboard Output [icon: file-text, label: "Dashboard/Report Output"]

Power BI Dashboard [icon: powerbi, label: "Power BI (Microsoft)"]

Power BI Note [icon:info, label:"All reporting and compliance dashboards are powered by Microsoft Power BI."]

}



// AZURE CLOUD SERVICES LAYER

Azure Cloud Services [color: gray, icon: cloud] {

Azure OpenAI Foundry [icon: azure-openai, label: "OpenAI (Foundry)"]

Azure Cosmos DB [icon: azure-cosmos-db, label: "Cosmos DB"]

Azure Key Vault [icon: azure-key-vault, label: "Key Vault"]

Monitoring & Audit [icon: activity, label: "Monitoring & Audit"]

KeyVaultCallout [label: "All agents retrieve credentials from Azure Key Vault.", icon: info]

}



// MAIN WORKFLOW (solid arrows)

Security Analyst > User Portal : "user actions"

User Portal > Orchestrator AI Agent : "trigger workflow"

Ticketing Agent > Reporting AI Agent : "remediation ticket"

Reporting AI Agent > Dashboard Output : "report"

Reporting AI Agent > Power BI Dashboard : "exec dashboard"

Dashboard Output > Power BI Dashboard : "dashboard sync"



// AI/LLM CALLS

Triage & Risk Scoring AI Agent > Azure OpenAI Foundry : "AI risk scoring"

Reporting AI Agent > Azure OpenAI Foundry : "AI summary"



// LOGGING (dashed arrows)

Review & Approval --> Azure Cosmos DB : "log approval"

Ticketing Agent --> Azure Cosmos DB : "log ticket"



// KEY VAULT SECRETS (dotted arrows)

"Nexpose AI Agent ...> Azure Key Vault : "get secrets""

"Wiz AI Agent ...> Azure Key Vault : "get secrets""

"Defender AI Agent ...> Azure Key Vault : "get secrets""

"WebApp Scanner AI Agent ...> Azure Key Vault : "get secrets""

"Ticketing Agent ...> Azure Key Vault : "get secrets""

"Orchestrator AI Agent ...> Azure Key Vault : "get secrets""



// MONITORING & AUDIT (dotted/dashed arrows)

"Azure Cosmos DB ...> Monitoring & Audit : "audit log""

"Orchestrator AI Agent ...> Monitoring & Audit : "monitor ops""

"Reporting AI Agent ...> Monitoring & Audit : "report delivery""

"Power BI Dashboard ...> Monitoring & Audit : "dashboard access""

Azure Cosmos DB --> Monitoring & Audit: "audit/monitor logs"

Ingestion Agents <> Deduplication & Normalization: "vuln data"

Deduplication & Normalization --> Azure Cosmos DB: "log"

Enrichment AI Agent --> Azure Cosmos DB: "log"

Triage & Risk Scoring AI Agent --> Azure Cosmos DB: "log"

Reporting AI Agent --> Azure Cosmos DB: "log"

Dashboard Output --> Azure Cosmos DB: "log"

Power BI Dashboard --> Azure Cosmos DB: "log"

Processing > Human Review: "prioritized"

Human Review > Remediation & Reporting: "approved"

Orchestration Layer > Azure Key Vault: "retrieve keys"

Ingestion Agents > Azure Key Vault: "retrieve keys"

Enrichment AI Agent > Azure Key Vault: "retrieve keys"

Triage & Risk Scoring AI Agent > Azure Key Vault: "retrieve keys"

Reporting AI Agent > Azure Key Vault: "retrieve keys"

Orchestration Layer > Ingestion Agents: trigger ingestion

Deduplication & Normalization > Enrichment AI Agent: "normalized"

Enrichment AI Agent > Triage & Risk Scoring AI Agent: enriched



