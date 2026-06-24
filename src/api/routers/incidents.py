from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas import (
    CreateIncidentRequest,
    CreateInvestigationRequest,
    CreateEvidenceRequest,
)
from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.commands.create_investigation_command import (
    CreateInvestigationCommand,
)
from src.application.factories.incident_factory import (
    create_incident_use_case,
    get_incident_use_case,
    create_investigation_use_case,
    create_evidence_use_case,

)
from src.infrastructure.database.dependencies import (
    get_db_session,
)

from src.application.commands.create_evidence_command import (
    CreateEvidenceCommand,
)

router = APIRouter()


@router.post("/incidents")
async def create_incident(
    request: CreateIncidentRequest,
):

    async for session in get_db_session():

        use_case = create_incident_use_case(
            session,
        )

        command = CreateIncidentCommand(
            title=request.title,
            description=request.description,
            service_name=request.service_name,
            severity=request.severity,
        )

        result = await use_case.execute(
            command
        )

        return result
    
@router.get(
    "/incidents/{incident_id}"
)
async def get_incident(
    incident_id: str,
):

    async for session in get_db_session():

        use_case = get_incident_use_case(
            session,
        )

        result = await use_case.execute(
            incident_id,
        )

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Incident not found",
            )

        return result
    
@router.post(
    "/investigations"
)
async def create_investigation(
    request: CreateInvestigationRequest,
):

    async for session in get_db_session():

        use_case = create_investigation_use_case(
            session,
        )

        command = CreateInvestigationCommand(
            incident_id=request.incident_id,
        )

        result = await use_case.execute(
            command,
        )

        return result
    
@router.post("/evidence")
async def create_evidence(
    request: CreateEvidenceRequest,
):

    async for session in get_db_session():

        use_case = create_evidence_use_case(
            session,
        )

        command = CreateEvidenceCommand(
            investigation_id=request.investigation_id,
            source=request.source,
            content=request.content,
            confidence_score=request.confidence_score,
        )

        result = await use_case.execute(
            command,
        )

        return result