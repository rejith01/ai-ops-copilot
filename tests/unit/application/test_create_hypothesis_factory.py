from unittest.mock import MagicMock

from src.application.factories.incident_factory import (
    create_hypothesis_use_case,
)


def test_create_hypothesis_factory():

    session = MagicMock()

    use_case = create_hypothesis_use_case(
        session,
    )

    assert use_case is not None