from unittest.mock import AsyncMock

from src.application.factories.incident_factory import (
    create_rollback_plan_use_case,
)


def test_create_rollback_plan_factory():

    session = AsyncMock()

    use_case = create_rollback_plan_use_case(
        session,
    )

    assert use_case is not None