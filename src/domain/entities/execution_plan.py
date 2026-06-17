from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.execution_plan_id import ExecutionPlanId


@dataclass
class ExecutionPlan:
    execution_plan_id: ExecutionPlanId

    title: str
    description: str

    actions: list[str]

    status: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

        if not self.description.strip():
            raise ValueError("Description cannot be empty")

        if len(self.actions) == 0:
            raise ValueError(
                "Execution plan must contain at least one action"
            )

    def transition_to(self, new_status: str):
        allowed_transitions = {
            "DRAFT": {"VALIDATED"},
            "VALIDATED": {"SIMULATED"},
            "SIMULATED": {"APPROVED"},
            "APPROVED": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()