from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RollbackPlanDTO:
    rollback_plan_id: str

    execution_plan_id: str

    steps: list[str]

    status: str

    created_at: datetime
    updated_at: datetime