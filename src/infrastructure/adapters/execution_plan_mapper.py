from uuid import UUID

from src.domain.entities.execution_plan import (
    ExecutionPlan,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)
from src.infrastructure.database.models.execution_plan_model import (
    ExecutionPlanModel,
)


class ExecutionPlanMapper:

    @staticmethod
    def to_model(
        execution_plan: ExecutionPlan,
    ) -> ExecutionPlanModel:

        return ExecutionPlanModel(
            execution_plan_id=str(
                execution_plan.execution_plan_id.value
            ),
            title=execution_plan.title,
            description=execution_plan.description,
            actions=execution_plan.actions,
            status=execution_plan.status,
            created_at=execution_plan.created_at,
            updated_at=execution_plan.updated_at,
        )

    @staticmethod
    def to_domain(
        model: ExecutionPlanModel,
    ) -> ExecutionPlan:

        return ExecutionPlan(
            execution_plan_id=ExecutionPlanId(
                UUID(
                    model.execution_plan_id
                )
            ),
            title=model.title,
            description=model.description,
            actions=model.actions,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )