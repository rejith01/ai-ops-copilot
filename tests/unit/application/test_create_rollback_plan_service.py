from unittest.mock import AsyncMock

import pytest

from src.application.commands.create_rollback_plan_command import (
    CreateRollbackPlanCommand,
)
from src.application.services.create_rollback_plan_service import (
    CreateRollbackPlanService,
)


@pytest.mark.asyncio
async def test_create_rollback_plan():

    repository = AsyncMock()

    service = CreateRollbackPlanService(
        repository,
    )

    command = CreateRollbackPlanCommand(
    execution_plan_id="123e4567-e89b-12d3-a456-426614174000",
    steps=[
        "Stop service",
        "Restore backup",
        "Start service",
    ],
    )

    result = await service.execute(
        command,
    )

    repository.save.assert_awaited_once()

    assert (
    result.execution_plan_id
    == "123e4567-e89b-12d3-a456-426614174000"
)

    assert result.steps == [
    "Stop service",
    "Restore backup",
    "Start service",
]

    assert result.status == "DRAFT"