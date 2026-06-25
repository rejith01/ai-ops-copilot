from uuid import UUID

from src.domain.entities.rollback_plan import (
    RollbackPlan,
)
from src.domain.value_objects.rollback_plan_id import (
    RollbackPlanId,
)
from src.infrastructure.database.models.rollback_plan_model import (
    RollbackPlanModel,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)


class RollbackPlanMapper:

    @staticmethod
    def to_model(
        rollback_plan: RollbackPlan,
    ) -> RollbackPlanModel:

        return RollbackPlanModel(
    rollback_plan_id=str(
        rollback_plan.rollback_plan_id.value
    ),
    execution_plan_id=str(
        rollback_plan.execution_plan_id.value
    ),
    steps=rollback_plan.steps,
    status=rollback_plan.status,
    created_at=rollback_plan.created_at,
    updated_at=rollback_plan.updated_at,
)

    @staticmethod
    def to_domain(
        model: RollbackPlanModel,
    ) -> RollbackPlan:

        return RollbackPlan(
    rollback_plan_id=RollbackPlanId(
        UUID(
            model.rollback_plan_id
        )
    ),
    execution_plan_id=ExecutionPlanId(
        UUID(
            model.execution_plan_id
        )
    ),
    steps=model.steps,
    status=model.status,
    created_at=model.created_at,
    updated_at=model.updated_at,
)