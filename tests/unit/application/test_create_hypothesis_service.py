import pytest

from src.application.commands.create_hypothesis_command import (
    CreateHypothesisCommand,
)
from src.application.services.create_hypothesis_service import (
    CreateHypothesisService,
)


class FakeHypothesisRepository:

    async def save(
        self,
        hypothesis,
    ):
        self.saved_hypothesis = hypothesis

    async def get_by_id(
        self,
        hypothesis_id,
    ):
        return None


@pytest.mark.asyncio
async def test_create_hypothesis():

    repository = FakeHypothesisRepository()

    service = CreateHypothesisService(
        repository,
    )

    command = CreateHypothesisCommand(
        investigation_id="11111111-1111-1111-1111-111111111111",
        description="Database connection pool exhausted",
        confidence_score=0.92,
    )

    result = await service.execute(
        command
    )

    assert (
        result.description
        == "Database connection pool exhausted"
    )

    assert result.status == "GENERATED"