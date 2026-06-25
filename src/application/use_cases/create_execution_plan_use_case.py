from src.application.commands.create_execution_plan_command import (
    CreateExecutionPlanCommand,
)
from src.application.dto.execution_plan_dto import (
    ExecutionPlanDTO,
)
from src.application.services.create_execution_plan_service import (
    CreateExecutionPlanService,
)


class CreateExecutionPlanUseCase:

    def __init__(
        self,
        service: CreateExecutionPlanService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateExecutionPlanCommand,
    ) -> ExecutionPlanDTO:

        return await self._service.execute(
            command
        )