from datetime import datetime
from uuid import uuid4

from src.application.commands.create_execution_plan_command import (
    CreateExecutionPlanCommand,
)
from src.application.dto.execution_plan_dto import (
    ExecutionPlanDTO,
)
from src.domain.entities.execution_plan import (
    ExecutionPlan,
)
from src.domain.interfaces.execution_plan_repository import (
    ExecutionPlanRepository,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)


class CreateExecutionPlanService:

    def __init__(
        self,
        repository: ExecutionPlanRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateExecutionPlanCommand,
    ) -> ExecutionPlanDTO:

        now = datetime.utcnow()

        execution_plan = ExecutionPlan(
            execution_plan_id=ExecutionPlanId(
                uuid4()
            ),
            title=command.title,
            description=command.description,
            actions=command.actions,
            status="DRAFT",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            execution_plan
        )

        return ExecutionPlanDTO(
            execution_plan_id=str(
                execution_plan.execution_plan_id.value
            ),
            title=execution_plan.title,
            description=execution_plan.description,
            actions=execution_plan.actions,
            status=execution_plan.status,
            created_at=execution_plan.created_at,
            updated_at=execution_plan.updated_at,
        )