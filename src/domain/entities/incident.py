from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.incident_id import IncidentId

@dataclass
class Incident:
    incident_id: IncidentId
    title: str
    description: str
    service_name: str
    severity: str
    status: str
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        allowed_severities = {"P1", "P2", "P3", "P4"}

        if self.severity not in allowed_severities:
            raise ValueError(
                f"Invalid severity: {self.severity}"
            )
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

        if not self.service_name.strip():
            raise ValueError("Service name cannot be empty")
        
    def transition_to(self, new_status: str):
        allowed_transitions = {
        "OPEN": {"INVESTIGATING"},
        "INVESTIGATING": {"HYPOTHESIS_GENERATED"},
        "HYPOTHESIS_GENERATED": {"REMEDIATION_PLANNED"},
        "REMEDIATION_PLANNED": {"APPROVED"},
        "APPROVED": {"SIMULATED"},
        "SIMULATED": {"RESOLVED"},
        "RESOLVED": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
        )

        self.status = new_status
        self.updated_at = datetime.utcnow()