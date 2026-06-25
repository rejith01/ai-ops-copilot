from dataclasses import dataclass


@dataclass(frozen=True)
class CreateRollbackPlanCommand:
    execution_plan_id: str

    steps: list[str]