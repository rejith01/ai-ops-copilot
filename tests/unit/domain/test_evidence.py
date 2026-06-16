from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.evidence import Evidence
from src.domain.value_objects.evidence_id import EvidenceId
from src.domain.value_objects.investigation_id import InvestigationId


def test_invalid_confidence_score_raises_error():
    with pytest.raises(ValueError):
        Evidence(
            evidence_id=EvidenceId(uuid4()),
            investigation_id=InvestigationId(uuid4()),
            source="CloudWatch",
            content="CPU usage 99%",
            confidence_score=1.5,
            status="COLLECTED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_source_raises_error():
    with pytest.raises(ValueError, match="Source cannot be empty"):
        Evidence(
            evidence_id=EvidenceId(uuid4()),
            investigation_id=InvestigationId(uuid4()),
            source="",
            content="CPU usage 99%",
            confidence_score=0.9,
            status="COLLECTED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    evidence = Evidence(
        evidence_id=EvidenceId(uuid4()),
        investigation_id=InvestigationId(uuid4()),
        source="CloudWatch",
        content="CPU usage 99%",
        confidence_score=0.9,
        status="COLLECTED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    evidence.transition_to("VALIDATED")

    assert evidence.status == "VALIDATED"


def test_invalid_status_transition_raises_error():
    evidence = Evidence(
        evidence_id=EvidenceId(uuid4()),
        investigation_id=InvestigationId(uuid4()),
        source="CloudWatch",
        content="CPU usage 99%",
        confidence_score=0.9,
        status="VALIDATED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        evidence.transition_to("COLLECTED")