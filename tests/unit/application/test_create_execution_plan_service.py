from unittest.mock import AsyncMock

import pytest

from src.application.commands.create_execution_plan_command import (
    CreateExecutionPlanCommand,
)
from src.application.services.create_execution_plan_service import (
    CreateExecutionPlanService,
)


@pytest.mark.asyncio
async def test_create_execution_plan():

    repository = AsyncMock()

    service = CreateExecutionPlanService(
        repository,
    )

    command = CreateExecutionPlanCommand(
        title="Restart Database",
        description="Restart PostgreSQL service",
        actions=[
            "Drain connections",
            "Restart postgres",
            "Verify health",
        ],
    )

    result = await service.execute(
        command,
    )

    repository.save.assert_awaited_once()

    assert result.title == "Restart Database"
    assert result.status == "DRAFT"