from src.application.commands.create_evidence_command import (
    CreateEvidenceCommand,
)
from src.application.dto.evidence_dto import (
    EvidenceDTO,
)
from src.application.services.create_evidence_service import (
    CreateEvidenceService,
)


class CreateEvidenceUseCase:

    def __init__(
        self,
        service: CreateEvidenceService,
    ):
        self._service = service

    async def execute(
        self,
        command: CreateEvidenceCommand,
    ) -> EvidenceDTO:

        return await self._service.execute(
            command
        )