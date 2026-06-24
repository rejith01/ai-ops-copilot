import pytest

from src.application.commands.create_hypothesis_command import (
    CreateHypothesisCommand,
)
from src.application.services.create_hypothesis_service import (
    CreateHypothesisService,
)
from src.application.use_cases.create_hypothesis_use_case import (
    CreateHypothesisUseCase,
)


class FakeHypothesisRepository:

    async def save(
        self,
        hypothesis,
    ):
        pass

    async def get_by_id(
        self,
        hypothesis_id,
    ):
        return None


@pytest.mark.asyncio
async def test_create_hypothesis_use_case():

    repository = FakeHypothesisRepository()

    service = CreateHypothesisService(
        repository,
    )

    use_case = CreateHypothesisUseCase(
        service,
    )

    command = CreateHypothesisCommand(
        investigation_id="11111111-1111-1111-1111-111111111111",
        description="Database connection pool exhausted",
        confidence_score=0.92,
    )

    result = await use_case.execute(
        command
    )

    assert result.status == "GENERATED"