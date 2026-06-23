from uuid import UUID

from src.application.dto.incident_dto import IncidentDTO
from src.domain.interfaces.incident_repository import (
    IncidentRepository,
)
from src.domain.value_objects.incident_id import (
    IncidentId,
)


class GetIncidentUseCase:

    def __init__(
        self,
        repository: IncidentRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        incident_id: str,
    ) -> IncidentDTO | None:

        incident = await self._repository.get_by_id(
            IncidentId(
                UUID(incident_id)
            )
        )

        if incident is None:
            return None

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