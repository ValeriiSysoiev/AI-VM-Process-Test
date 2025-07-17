# ISO Control Mapping

The table below shows how the main components of the Vulnerability Management Orchestration template align with key ISO security controls. Clause numbers refer to the 2022 revision of ISO/IEC 27001 and the 2023/2025 drafts of ISO/IEC 42001 and ISO/IEC 42005. Only control references are provided here for traceability.

| Solution Component | ISO/IEC 27001:2022 Controls | ISO/IEC 42001:2023 Controls | ISO/IEC 42005:2025 Controls |
|--------------------|-----------------------------|-----------------------------|-----------------------------|
| **User Portal (Web UI)** | A.5.15.1, A.5.16.1 (access control & authentication) | Clause 5.2, Annex A.3.2.2 (human oversight) | Accountability & traceability |
| **Orchestrator AI Agent** | A.8.28.1, A.8.32.1 (secure operations & change control) | Clause 6.2, Annex A.6.3.1 (AI lifecycle management) | Core Process 4.1 (control design) |
| **Ingestion Agents** | A.5.1.1, A.5.3.1, A.8.9.1 (policy, duties, input validation) | Clause 6.1, Annex A.2.2 (risk assessment & data sourcing) | Impact assessment & data intake |
| **Processing Agents** | A.8.10.1, A.8.28.1 (input validation, secure development) | Annex A.6.2 (secure AI design) | Control mitigation planning |
| **Triage & Risk AI Agent** | A.8.23.1, A.8.29.1 (information validation, technical review) | Annex A.6.2.4, Annex A.8.3.2 (model risk management) | Risk identification & treatment |
| **Human-in-the-Loop Oversight** | A.5.3.1 (segregation of duties), A.5.11.1 (responsibility) | Clause 5.2, Annex A.3.2.2 | Governance roles & accountability |
| **Remediation Agent** | A.8.29.1, A.8.30.1 (change management, operational planning) | Clause 8.3.1 (operational control) | Mitigation implementation |
| **Reporting Agent** | A.5.20.1, A.5.21.1 (logging and monitoring) | Clause 9.1 (performance evaluation) | Control monitoring |
| **Azure Key Vault & Secrets Management** | A.8.24.1, A.8.28.1 (key management, secure storage) | Annex A.6.2.4 | Secure model & key protection |
| **Logging & Audit (Cosmos DB / Log Analytics)** | A.5.17.1, A.5.18.1 (logging and audit) | Annex A.6.2.4, Annex A.8.3.2 | Accountability & traceability |
| **CI/CD & Infrastructure-as-Code** | A.8.28.1, A.8.32.1 (secure development & deployments) | Clause 6.2, Annex A.6.2 | Lifecycle risk management |
| **Model Management (LLM / Foundry)** | A.8.28.1, A.8.32.1 (model integrity, code review) | Annex A.6.2, Annex A.8.3.1 | AI model risk & impact |

*This mapping serves as a starting point and should be expanded or tailored for specific compliance assessments.*
