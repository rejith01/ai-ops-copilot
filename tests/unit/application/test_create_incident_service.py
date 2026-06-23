import pytest

from src.application.commands.create_incident_command import (
    CreateIncidentCommand,
)
from src.application.services.create_incident_service import (
    CreateIncidentService,
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
async def test_create_incident():

    repository = FakeIncidentRepository()

    service = CreateIncidentService(
        repository,
    )

    command = CreateIncidentCommand(
        title="API Failure",
        description="Production API is down",
        service_name="payment-service",
        severity="P1",
    )

    result = await service.execute(
        command
    )

    assert result.title == "API Failure"
    assert result.service_name == "payment-service"
    assert result.severity == "P1"
    assert result.status == "OPEN"

    assert repository.saved_incident is not None