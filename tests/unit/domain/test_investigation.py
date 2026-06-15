from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.investigation import Investigation
from src.domain.value_objects.incident_id import IncidentId
from src.domain.value_objects.investigation_id import InvestigationId


def test_valid_status_transition():
    investigation = Investigation(
        investigation_id=InvestigationId(uuid4()),
        incident_id=IncidentId(uuid4()),
        status="CREATED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    investigation.transition_to("COLLECTING_EVIDENCE")

    assert investigation.status == "COLLECTING_EVIDENCE"


def test_invalid_status_transition_raises_error():
    investigation = Investigation(
        investigation_id=InvestigationId(uuid4()),
        incident_id=IncidentId(uuid4()),
        status="CREATED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        investigation.transition_to("COMPLETED")