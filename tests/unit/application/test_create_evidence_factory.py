from unittest.mock import MagicMock

from src.application.factories.incident_factory import (
    create_evidence_use_case,
)
from src.application.use_cases.create_evidence_use_case import (
    CreateEvidenceUseCase,
)


def test_create_evidence_factory():

    session = MagicMock()

    use_case = create_evidence_use_case(
        session,
    )

    assert isinstance(
        use_case,
        CreateEvidenceUseCase,
    )