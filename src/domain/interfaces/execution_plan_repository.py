from abc import ABC
from abc import abstractmethod

from src.domain.entities.execution_plan import (
    ExecutionPlan,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)


class ExecutionPlanRepository(
    ABC,
):

    @abstractmethod
    async def save(
        self,
        execution_plan: ExecutionPlan,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        execution_plan_id: ExecutionPlanId,
    ) -> ExecutionPlan | None:
        pass