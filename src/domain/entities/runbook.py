from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.runbook_id import RunbookId


@dataclass
class Runbook:
    runbook_id: RunbookId

    title: str
    description: str

    steps: list[str]

    status: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

        if not self.description.strip():
            raise ValueError("Description cannot be empty")

        if len(self.steps) == 0:
            raise ValueError(
                "Runbook must contain at least one step"
            )

    def transition_to(self, new_status: str):
        allowed_transitions = {
            "DRAFT": {"REVIEWED"},
            "REVIEWED": {"APPROVED"},
            "APPROVED": {"ACTIVE"},
            "ACTIVE": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()