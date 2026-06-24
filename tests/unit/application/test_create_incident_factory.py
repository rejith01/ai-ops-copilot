from unittest.mock import MagicMock

from src.application.factories.incident_factory import (
    create_incident_use_case,
)
from src.application.use_cases.create_incident_use_case import (
    CreateIncidentUseCase,
)


def test_create_incident_factory():

    session = MagicMock()

    use_case = create_incident_use_case(
        session,
    )

    assert isinstance(
        use_case,
        CreateIncidentUseCase,
    )