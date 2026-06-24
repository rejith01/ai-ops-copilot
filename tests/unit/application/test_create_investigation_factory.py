from unittest.mock import MagicMock

from src.application.factories.incident_factory import (
    create_investigation_use_case,
)
from src.application.use_cases.create_investigation_use_case import (
    CreateInvestigationUseCase,
)


def test_create_investigation_factory():

    session = MagicMock()

    use_case = create_investigation_use_case(
        session,
    )

    assert isinstance(
        use_case,
        CreateInvestigationUseCase,
    )