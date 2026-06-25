from unittest.mock import AsyncMock

import pytest

from src.application.commands.create_execution_plan_command import (
    CreateExecutionPlanCommand,
)
from src.application.use_cases.create_execution_plan_use_case import (
    CreateExecutionPlanUseCase,
)


@pytest.mark.asyncio
async def test_create_execution_plan_use_case():

    service = AsyncMock()

    use_case = CreateExecutionPlanUseCase(
        service,
    )

    command = CreateExecutionPlanCommand(
        title="Restart Database",
        description="Restart PostgreSQL service",
        actions=[
            "Restart",
        ],
    )

    await use_case.execute(
        command,
    )

    service.execute.assert_awaited_once_with(
        command,
    )