from sqlalchemy.ext.asyncio import AsyncSession

from src.application.services.create_incident_service import (
    CreateIncidentService,
)
from src.application.use_cases.create_incident_use_case import (
    CreateIncidentUseCase,
)
from src.infrastructure.repositories.incident_repository import (
    IncidentRepositorySQLAlchemy,
)


def create_incident_use_case(
    session: AsyncSession,
) -> CreateIncidentUseCase:

    repository = IncidentRepositorySQLAlchemy(
        session,
    )

    service = CreateIncidentService(
        repository,
    )

    return CreateIncidentUseCase(
        service,
    )