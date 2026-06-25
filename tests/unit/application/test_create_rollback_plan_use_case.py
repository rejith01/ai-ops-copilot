from unittest.mock import AsyncMock

import pytest

from src.application.commands.create_rollback_plan_command import (
    CreateRollbackPlanCommand,
)
from src.application.use_cases.create_rollback_plan_use_case import (
    CreateRollbackPlanUseCase,
)


@pytest.mark.asyncio
async def test_create_rollback_plan_use_case():

    service = AsyncMock()

    use_case = CreateRollbackPlanUseCase(
        service,
    )

    command = CreateRollbackPlanCommand(
    execution_plan_id="123e4567-e89b-12d3-a456-426614174000",
    steps=[
        "Restore backup",
    ],
    )

    await use_case.execute(
        command,
    )

    service.execute.assert_awaited_once_with(
        command,
    )