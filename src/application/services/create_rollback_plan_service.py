from datetime import datetime
from uuid import UUID
from uuid import uuid4

from src.application.commands.create_rollback_plan_command import (
    CreateRollbackPlanCommand,
)
from src.application.dto.rollback_plan_dto import (
    RollbackPlanDTO,
)
from src.domain.entities.rollback_plan import (
    RollbackPlan,
)
from src.domain.interfaces.rollback_plan_repository import (
    RollbackPlanRepository,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)
from src.domain.value_objects.rollback_plan_id import (
    RollbackPlanId,
)


class CreateRollbackPlanService:

    def __init__(
        self,
        repository: RollbackPlanRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateRollbackPlanCommand,
    ) -> RollbackPlanDTO:

        now = datetime.utcnow()

        rollback_plan = RollbackPlan(
            rollback_plan_id=RollbackPlanId(
                uuid4()
            ),
            execution_plan_id=ExecutionPlanId(
                UUID(
                    command.execution_plan_id
                )
            ),
            steps=command.steps,
            status="DRAFT",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            rollback_plan
        )

        return RollbackPlanDTO(
            rollback_plan_id=str(
                rollback_plan.rollback_plan_id.value
            ),
            execution_plan_id=str(
                rollback_plan.execution_plan_id.value
            ),
            steps=rollback_plan.steps,
            status=rollback_plan.status,
            created_at=rollback_plan.created_at,
            updated_at=rollback_plan.updated_at,
        )