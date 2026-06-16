from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.hypothesis_id import HypothesisId
from src.domain.value_objects.investigation_id import InvestigationId


@dataclass
class RootCauseHypothesis:
    hypothesis_id: HypothesisId
    investigation_id: InvestigationId

    description: str
    confidence_score: float

    status: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.description.strip():
            raise ValueError("Description cannot be empty")

        if not 0.0 <= self.confidence_score <= 1.0:
            raise ValueError(
                f"Invalid confidence score: {self.confidence_score}"
            )

    def transition_to(self, new_status: str):
        allowed_transitions = {
            "GENERATED": {"VALIDATED", "REJECTED"},
            "VALIDATED": set(),
            "REJECTED": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()