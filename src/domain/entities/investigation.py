from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.investigation_id import InvestigationId
from src.domain.value_objects.incident_id import IncidentId


@dataclass
class Investigation:
    investigation_id: InvestigationId
    incident_id: IncidentId

    status: str

    created_at: datetime
    updated_at: datetime

    def transition_to(self, new_status: str):
        allowed_transitions = {
        "CREATED": {"COLLECTING_EVIDENCE"},
        "COLLECTING_EVIDENCE": {"ANALYZING"},
        "ANALYZING": {"COMPLETED"},
        "COMPLETED": set(),
    }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()