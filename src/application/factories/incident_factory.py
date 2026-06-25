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
from src.application.services.create_hypothesis_service import (
    CreateHypothesisService,
)

from src.application.use_cases.create_hypothesis_use_case import (
    CreateHypothesisUseCase,
)

from src.infrastructure.repositories.hypothesis_repository import (
    HypothesisRepositorySQLAlchemy,
)

from src.application.services.create_execution_plan_service import (
    CreateExecutionPlanService,
)

from src.application.use_cases.create_execution_plan_use_case import (
    CreateExecutionPlanUseCase,
)

from src.infrastructure.repositories.execution_plan_repository import (
    ExecutionPlanRepositorySQLAlchemy,
)

from src.application.services.create_rollback_plan_service import (
    CreateRollbackPlanService,
)

from src.application.use_cases.create_rollback_plan_use_case import (
    CreateRollbackPlanUseCase,
)

from src.infrastructure.repositories.rollback_plan_repository import (
    RollbackPlanRepositorySQLAlchemy,
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

def create_hypothesis_use_case(
    session: AsyncSession,
) -> CreateHypothesisUseCase:

    repository = HypothesisRepositorySQLAlchemy(
        session,
    )

    service = CreateHypothesisService(
        repository,
    )

    return CreateHypothesisUseCase(
        service,
    )

def create_execution_plan_use_case(
    session: AsyncSession,
) -> CreateExecutionPlanUseCase:

    repository = ExecutionPlanRepositorySQLAlchemy(
        session,
    )

    service = CreateExecutionPlanService(
        repository,
    )

    return CreateExecutionPlanUseCase(
        service,
    )

def create_rollback_plan_use_case(
    session: AsyncSession,
) -> CreateRollbackPlanUseCase:

    repository = RollbackPlanRepositorySQLAlchemy(
        session,
    )

    service = CreateRollbackPlanService(
        repository,
    )

    return CreateRollbackPlanUseCase(
        service,
    )