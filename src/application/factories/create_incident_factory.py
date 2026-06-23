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
from src.application.use_cases.get_incident_use_case import (
    GetIncidentUseCase,
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

def get_incident_use_case(
    session: AsyncSession,
) -> GetIncidentUseCase:

    repository = IncidentRepositorySQLAlchemy(
        session,
    )

    return GetIncidentUseCase(
        repository,
    )