from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.incident import Incident
from src.domain.value_objects.incident_id import IncidentId


def test_invalid_severity_raises_error():
    with pytest.raises(ValueError):
        Incident(
            incident_id=IncidentId(uuid4()),
            title="Database outage",
            description="Primary DB unavailable",
            service_name="postgres",
            severity="P5",
            status="OPEN",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
def test_empty_title_raises_error():
    with pytest.raises(ValueError,match="Title cannot be empty"):
        Incident(
            incident_id=IncidentId(uuid4()),
            title="",
            description="Primary DB unavailable",
            service_name="postgres",
            severity="P1",
            status="OPEN",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

def test_empty_service_name_raises_error():
    with pytest.raises(ValueError, match="Service name cannot be empty"):
        Incident(
            incident_id=IncidentId(uuid4()),
            title="Database outage",
            description="Primary DB unavailable",
            service_name="",
            severity="P1",
            status="OPEN",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
def test_valid_status_transition():
    incident = Incident(
        incident_id=IncidentId(uuid4()),
        title="Database outage",
        description="Primary DB unavailable",
        service_name="postgres",
        severity="P1",
        status="OPEN",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    incident.transition_to("INVESTIGATING")

    assert incident.status == "INVESTIGATING"

def test_invalid_status_transition_raises_error():
    incident = Incident(
        incident_id=IncidentId(uuid4()),
        title="Database outage",
        description="Primary DB unavailable",
        service_name="postgres",
        severity="P1",
        status="OPEN",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        incident.transition_to("RESOLVED")
