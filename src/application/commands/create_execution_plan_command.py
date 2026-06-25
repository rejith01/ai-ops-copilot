from dataclasses import dataclass


@dataclass(frozen=True)
class CreateExecutionPlanCommand:
    title: str
    description: str

    actions: list[str]