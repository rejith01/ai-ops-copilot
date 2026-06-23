from datetime import datetime
from uuid import uuid4

from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.dto.incident_dto import (
    IncidentDTO,
)
from src.domain.entities.incident import Incident
from src.domain.interfaces.incident_repository import (
    IncidentRepository,
)
from src.domain.value_objects.incident_id import (
    IncidentId,
)


class CreateIncidentService:

    def __init__(
        self,
        repository: IncidentRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateIncidentCommand,
    ) -> IncidentDTO:

        now = datetime.utcnow()

        incident = Incident(
            incident_id=IncidentId(
                uuid4()
            ),
            title=command.title,
            description=command.description,
            service_name=command.service_name,
            severity=command.severity,
            status="OPEN",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            incident
        )

        return IncidentDTO(
            incident_id=str(
                incident.incident_id.value
            ),
            title=incident.title,
            description=incident.description,
            service_name=incident.service_name,
            severity=incident.severity,
            status=incident.status,
            created_at=incident.created_at,
            updated_at=incident.updated_at,
        )