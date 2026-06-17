from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.rollback_plan import RollbackPlan
from src.domain.value_objects.execution_plan_id import ExecutionPlanId
from src.domain.value_objects.rollback_plan_id import RollbackPlanId


def test_rollback_plan_requires_at_least_one_step():
    with pytest.raises(
        ValueError,
        match="Rollback plan must contain at least one step"
    ):
        RollbackPlan(
            rollback_plan_id=RollbackPlanId(uuid4()),
            execution_plan_id=ExecutionPlanId(uuid4()),
            steps=[],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    plan = RollbackPlan(
        rollback_plan_id=RollbackPlanId(uuid4()),
        execution_plan_id=ExecutionPlanId(uuid4()),
        steps=["Scale deployment back to 2 replicas"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    plan.transition_to("READY")

    assert plan.status == "READY"


def test_invalid_status_transition_raises_error():
    plan = RollbackPlan(
        rollback_plan_id=RollbackPlanId(uuid4()),
        execution_plan_id=ExecutionPlanId(uuid4()),
        steps=["Scale deployment back to 2 replicas"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        plan.transition_to("EXECUTED")