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

from src.application.services.create_investigation_service import (
    CreateInvestigationService,
)

from src.application.use_cases.create_investigation_use_case import (
    CreateInvestigationUseCase,
)

from src.infrastructure.repositories.investigation_repository import (
    InvestigationRepositorySQLAlchemy,
)

from src.application.services.create_evidence_service import (
    CreateEvidenceService,
)

from src.application.use_cases.create_evidence_use_case import (
    CreateEvidenceUseCase,
)

from src.infrastructure.repositories.evidence_repository import (
    EvidenceRepositorySQLAlchemy,
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

def create_investigation_use_case(
    session: AsyncSession,
) -> CreateInvestigationUseCase:

    repository = InvestigationRepositorySQLAlchemy(
        session,
    )

    service = CreateInvestigationService(
        repository,
    )

    return CreateInvestigationUseCase(
        service,
    )

def create_evidence_use_case(
    session: AsyncSession,
) -> CreateEvidenceUseCase:

    repository = EvidenceRepositorySQLAlchemy(
        session,
    )

    service = CreateEvidenceService(
        repository,
    )

    return CreateEvidenceUseCase(
        service,
    )