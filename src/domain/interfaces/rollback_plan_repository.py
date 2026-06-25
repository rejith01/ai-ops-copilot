from abc import ABC
from abc import abstractmethod

from src.domain.entities.rollback_plan import (
    RollbackPlan,
)
from src.domain.value_objects.rollback_plan_id import (
    RollbackPlanId,
)


class RollbackPlanRepository(
    ABC,
):

    @abstractmethod
    async def save(
        self,
        rollback_plan: RollbackPlan,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        rollback_plan_id: RollbackPlanId,
    ) -> RollbackPlan | None:
        pass