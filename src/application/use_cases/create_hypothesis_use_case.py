from src.application.commands.create_hypothesis_command import (
    CreateHypothesisCommand,
)
from src.application.dto.hypothesis_dto import (
    HypothesisDTO,
)
from src.application.services.create_hypothesis_service import (
    CreateHypothesisService,
)


class CreateHypothesisUseCase:

    def __init__(
        self,
        service: CreateHypothesisService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateHypothesisCommand,
    ) -> HypothesisDTO:

        return await self._service.execute(
            command
        )