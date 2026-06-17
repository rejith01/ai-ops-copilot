from dataclasses import dataclass
from datetime import datetime

from src.domain.value_objects.rollback_plan_id import RollbackPlanId
from src.domain.value_objects.execution_plan_id import ExecutionPlanId


@dataclass
class RollbackPlan:
    rollback_plan_id: RollbackPlanId
    execution_plan_id: ExecutionPlanId

    steps: list[str]

    status: str

    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        if len(self.steps) == 0:
            raise ValueError(
                "Rollback plan must contain at least one step"
            )

    def transition_to(self, new_status: str):
        allowed_transitions = {
            "DRAFT": {"READY"},
            "READY": {"EXECUTED"},
            "EXECUTED": set(),
        }

        if new_status not in allowed_transitions[self.status]:
            raise ValueError(
                f"Invalid status transition: {self.status} -> {new_status}"
            )

        self.status = new_status
        self.updated_at = datetime.utcnow()