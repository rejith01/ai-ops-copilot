from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ExecutionPlanDTO:
    execution_plan_id: str

    title: str
    description: str

    actions: list[str]

    status: str

    created_at: datetime
    updated_at: datetime