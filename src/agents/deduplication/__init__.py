from src.templates import BaseAgent


class DeduplicationAgent(BaseAgent):
    """Remove duplicate findings."""

    def deduplicate(self, findings: list[dict]) -> list[dict]:
        unique = []
        seen = set()
        for finding in findings:
            vuln_id = finding.get("vuln_id")
            if vuln_id not in seen:
                seen.add(vuln_id)
                unique.append(finding)
        return unique
