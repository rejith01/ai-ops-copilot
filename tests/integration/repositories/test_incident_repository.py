from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.incident import Incident
from src.domain.value_objects.incident_id import IncidentId
from src.infrastructure.database.session import AsyncSessionLocal
from src.infrastructure.repositories.incident_repository import (
    IncidentRepositorySQLAlchemy,
)


@pytest.mark.asyncio
async def test_save_and_load_incident():

    async with AsyncSessionLocal() as session:

        repository = IncidentRepositorySQLAlchemy(
            session
        )

        incident = Incident(
            incident_id=IncidentId(uuid4()),
            title="Database Outage",
            description="Primary DB unavailable",
            service_name="postgres",
            severity="P1",
            status="OPEN",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        await repository.save(
            incident
        )

        loaded = await repository.get_by_id(
            incident.incident_id
        )

        assert loaded is not None

        assert (
            loaded.incident_id
            == incident.incident_id
        )

        assert (
            loaded.title
            == incident.title
        )

        assert (
            loaded.severity
            == incident.severity
        )
