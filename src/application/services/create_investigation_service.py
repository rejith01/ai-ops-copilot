from datetime import datetime
from uuid import UUID
from uuid import uuid4

from src.application.commands.create_investigation_command import (
    CreateInvestigationCommand,
)
from src.application.dto.investigation_dto import (
    InvestigationDTO,
)
from src.domain.entities.investigation import (
    Investigation,
)
from src.domain.interfaces.investigation_repository import (
    InvestigationRepository,
)
from src.domain.value_objects.incident_id import (
    IncidentId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)


class CreateInvestigationService:

    def __init__(
        self,
        repository: InvestigationRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateInvestigationCommand,
    ) -> InvestigationDTO:

        now = datetime.utcnow()

        investigation = Investigation(
            investigation_id=InvestigationId(
                uuid4()
            ),
            incident_id=IncidentId(
                UUID(
                    command.incident_id
                )
            ),
            status="CREATED",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            investigation
        )

        return InvestigationDTO(
            investigation_id=str(
                investigation.investigation_id.value
            ),
            incident_id=str(
                investigation.incident_id.value
            ),
            status=investigation.status,
            created_at=investigation.created_at,
            updated_at=investigation.updated_at,
        )