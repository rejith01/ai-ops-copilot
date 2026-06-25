from unittest.mock import AsyncMock

from src.application.factories.incident_factory import (
    create_execution_plan_use_case,
)


def test_create_execution_plan_factory():

    session = AsyncMock()

    use_case = create_execution_plan_use_case(
        session,
    )

    assert use_case is not None