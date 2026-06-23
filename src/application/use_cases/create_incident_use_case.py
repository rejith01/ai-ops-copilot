from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.dto.incident_dto import (
    IncidentDTO,
)
from src.application.services.create_incident_service import (
    CreateIncidentService,
)


class CreateIncidentUseCase:

    def __init__(
        self,
        service: CreateIncidentService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateIncidentCommand,
    ) -> IncidentDTO:
        return await self._service.execute(
            command
        )