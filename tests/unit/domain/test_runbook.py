from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.runbook import Runbook
from src.domain.value_objects.runbook_id import RunbookId


def test_empty_title_raises_error():
    with pytest.raises(
        ValueError,
        match="Title cannot be empty"
    ):
        Runbook(
            runbook_id=RunbookId(uuid4()),
            title="",
            description="Restart service",
            steps=["Check logs"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_description_raises_error():
    with pytest.raises(
        ValueError,
        match="Description cannot be empty"
    ):
        Runbook(
            runbook_id=RunbookId(uuid4()),
            title="Restart Service",
            description="",
            steps=["Check logs"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_runbook_requires_at_least_one_step():
    with pytest.raises(
        ValueError,
        match="Runbook must contain at least one step"
    ):
        Runbook(
            runbook_id=RunbookId(uuid4()),
            title="Restart Service",
            description="Restart service safely",
            steps=[],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    runbook = Runbook(
        runbook_id=RunbookId(uuid4()),
        title="Restart Service",
        description="Restart service safely",
        steps=["Check logs"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    runbook.transition_to("REVIEWED")

    assert runbook.status == "REVIEWED"


def test_invalid_status_transition_raises_error():
    runbook = Runbook(
        runbook_id=RunbookId(uuid4()),
        title="Restart Service",
        description="Restart service safely",
        steps=["Check logs"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        runbook.transition_to("ACTIVE")