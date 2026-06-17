from datetime import datetime
from uuid import uuid4

import pytest

from src.domain.entities.execution_plan import ExecutionPlan
from src.domain.value_objects.execution_plan_id import ExecutionPlanId


def test_empty_title_raises_error():
    with pytest.raises(
        ValueError,
        match="Title cannot be empty"
    ):
        ExecutionPlan(
            execution_plan_id=ExecutionPlanId(uuid4()),
            title="",
            description="Scale deployment",
            actions=["Scale to 5 replicas"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_empty_description_raises_error():
    with pytest.raises(
        ValueError,
        match="Description cannot be empty"
    ):
        ExecutionPlan(
            execution_plan_id=ExecutionPlanId(uuid4()),
            title="Scale Deployment",
            description="",
            actions=["Scale to 5 replicas"],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_execution_plan_requires_at_least_one_action():
    with pytest.raises(
        ValueError,
        match="Execution plan must contain at least one action"
    ):
        ExecutionPlan(
            execution_plan_id=ExecutionPlanId(uuid4()),
            title="Scale Deployment",
            description="Scale deployment safely",
            actions=[],
            status="DRAFT",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )


def test_valid_status_transition():
    plan = ExecutionPlan(
        execution_plan_id=ExecutionPlanId(uuid4()),
        title="Scale Deployment",
        description="Scale deployment safely",
        actions=["Scale to 5 replicas"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    plan.transition_to("VALIDATED")

    assert plan.status == "VALIDATED"


def test_invalid_status_transition_raises_error():
    plan = ExecutionPlan(
        execution_plan_id=ExecutionPlanId(uuid4()),
        title="Scale Deployment",
        description="Scale deployment safely",
        actions=["Scale to 5 replicas"],
        status="DRAFT",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    with pytest.raises(
        ValueError,
        match="Invalid status transition"
    ):
        plan.transition_to("APPROVED")