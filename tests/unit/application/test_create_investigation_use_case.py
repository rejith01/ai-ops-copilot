import pytest
from uuid import UUID

from src.application.commands.create_investigation_command import (
    CreateInvestigationCommand,
)
from src.application.services.create_investigation_service import (
    CreateInvestigationService,
)
from src.application.use_cases.create_investigation_use_case import (
    CreateInvestigationUseCase,
)
from src.domain.entities.investigation import (
    Investigation,
)
from src.domain.interfaces.investigation_repository import (
    InvestigationRepository,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)


class FakeInvestigationRepository(
    InvestigationRepository,
):

    def __init__(self):
        self.saved = None

    async def save(
        self,
        investigation: Investigation,
    ) -> None:
        self.saved = investigation

    async def get_by_id(
        self,
        investigation_id: InvestigationId,
    ):
        return self.saved


@pytest.mark.asyncio
async def test_create_investigation_use_case():

    repository = FakeInvestigationRepository()

    service = CreateInvestigationService(
        repository,
    )

    use_case = CreateInvestigationUseCase(
        service,
    )

    command = CreateInvestigationCommand(
        incident_id=str(UUID(int=1)),
    )

    result = await use_case.execute(
        command
    )

    assert result.status == "CREATED"