import pytest

from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.services.create_incident_service import (
    CreateIncidentService,
)
from src.application.use_cases.create_incident_use_case import (
    CreateIncidentUseCase,
)


class FakeIncidentRepository:

    def __init__(self):
        self.saved_incident = None

    async def save(
        self,
        incident,
    ):
        self.saved_incident = incident

    async def get_by_id(
        self,
        incident_id,
    ):
        return None


@pytest.mark.asyncio
async def test_create_incident_use_case():

    repository = FakeIncidentRepository()

    service = CreateIncidentService(
        repository,
    )

    use_case = CreateIncidentUseCase(
        service,
    )

    command = CreateIncidentCommand(
        title="Database Down",
        description="Primary DB unavailable",
        service_name="postgres",
        severity="P1",
    )

    result = await use_case.execute(
        command
    )

    assert result.title == "Database Down"
    assert result.status == "OPEN"

    assert repository.saved_incident is not None