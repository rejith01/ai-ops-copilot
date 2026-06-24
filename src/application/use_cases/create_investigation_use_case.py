from src.application.commands.create_investigation_command import (
    CreateInvestigationCommand,
)
from src.application.dto.investigation_dto import (
    InvestigationDTO,
)
from src.application.services.create_investigation_service import (
    CreateInvestigationService,
)


class CreateInvestigationUseCase:

    def __init__(
        self,
        service: CreateInvestigationService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateInvestigationCommand,
    ) -> InvestigationDTO:

        return await self._service.execute(
            command
        )