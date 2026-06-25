from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.execution_plan import (
    ExecutionPlan,
)
from src.domain.interfaces.execution_plan_repository import (
    ExecutionPlanRepository,
)
from src.domain.value_objects.execution_plan_id import (
    ExecutionPlanId,
)
from src.infrastructure.adapters.execution_plan_mapper import (
    ExecutionPlanMapper,
)
from src.infrastructure.database.models.execution_plan_model import (
    ExecutionPlanModel,
)


class ExecutionPlanRepositorySQLAlchemy(
    ExecutionPlanRepository,
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        execution_plan: ExecutionPlan,
    ) -> None:

        model = ExecutionPlanMapper.to_model(
            execution_plan
        )

        self._session.add(
            model
        )

        await self._session.commit()

    async def get_by_id(
        self,
        execution_plan_id: ExecutionPlanId,
    ) -> ExecutionPlan | None:

        stmt = select(
            ExecutionPlanModel
        ).where(
            ExecutionPlanModel.execution_plan_id
            == str(
                execution_plan_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return ExecutionPlanMapper.to_domain(
            model
        )