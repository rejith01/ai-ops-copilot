import pytest
from uuid import UUID

from src.application.commands.create_evidence_command import (
    CreateEvidenceCommand,
)
from src.application.services.create_evidence_service import (
    CreateEvidenceService,
)
from src.application.use_cases.create_evidence_use_case import (
    CreateEvidenceUseCase,
)
from src.domain.entities.evidence import (
    Evidence,
)
from src.domain.interfaces.evidence_repository import (
    EvidenceRepository,
)
from src.domain.value_objects.evidence_id import (
    EvidenceId,
)


class FakeEvidenceRepository(
    EvidenceRepository,
):

    def __init__(self):
        self.saved = None

    async def save(
        self,
        evidence: Evidence,
    ) -> None:
        self.saved = evidence

    async def get_by_id(
        self,
        evidence_id: EvidenceId,
    ):
        return self.saved


@pytest.mark.asyncio
async def test_create_evidence_use_case():

    repository = FakeEvidenceRepository()

    service = CreateEvidenceService(
        repository,
    )

    use_case = CreateEvidenceUseCase(
        service,
    )

    command = CreateEvidenceCommand(
        investigation_id=str(
            UUID(int=1)
        ),
        source="datadog",
        content="CPU spike detected",
        confidence_score=0.95,
    )

    result = await use_case.execute(
        command
    )

    assert result.status == "COLLECTED"

    assert result.source == "datadog"