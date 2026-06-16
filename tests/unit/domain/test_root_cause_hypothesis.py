from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.root_cause_hypothesis import RootCauseHypothesis
from src.domain.value_objects.hypothesis_id import HypothesisId
from src.domain.value_objects.investigation_id import InvestigationId


def test_invalid_confidence_score_raises_error():
    with pytest.raises(ValueError):
        RootCauseHypothesis(
            hypothesis_id=HypothesisId(uuid4()),
            investigation_id=InvestigationId(uuid4()),
            description="Database connection pool exhaustion",
            confidence_score=1.5,
            status="GENERATED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_description_raises_error():
    with pytest.raises(
        ValueError,
        match="Description cannot be empty"
    ):
        RootCauseHypothesis(
            hypothesis_id=HypothesisId(uuid4()),
            investigation_id=InvestigationId(uuid4()),
            description="",
            confidence_score=0.9,
            status="GENERATED",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    hypothesis = RootCauseHypothesis(
        hypothesis_id=HypothesisId(uuid4()),
        investigation_id=InvestigationId(uuid4()),
        description="Database connection pool exhaustion",
        confidence_score=0.9,
        status="GENERATED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    hypothesis.transition_to("VALIDATED")

    assert hypothesis.status == "VALIDATED"


def test_invalid_status_transition_raises_error():
    hypothesis = RootCauseHypothesis(
        hypothesis_id=HypothesisId(uuid4()),
        investigation_id=InvestigationId(uuid4()),
        description="Database connection pool exhaustion",
        confidence_score=0.9,
        status="VALIDATED",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        hypothesis.transition_to("GENERATED")