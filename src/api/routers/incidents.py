from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas import CreateIncidentRequest
from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.factories.create_incident_factory import (
    create_incident_use_case,
)
from src.infrastructure.database.dependencies import (
    get_db_session,
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