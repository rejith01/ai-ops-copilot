from src.application.commands.create_rollback_plan_command import (
    CreateRollbackPlanCommand,
)
from src.application.dto.rollback_plan_dto import (
    RollbackPlanDTO,
)
from src.application.services.create_rollback_plan_service import (
    CreateRollbackPlanService,
)


class CreateRollbackPlanUseCase:

    def __init__(
        self,
        service: CreateRollbackPlanService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateRollbackPlanCommand,
    ) -> RollbackPlanDTO:

        return await self._service.execute(
            command
        )