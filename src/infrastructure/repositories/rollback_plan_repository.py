from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.rollback_plan import (
    RollbackPlan,
)
from src.domain.interfaces.rollback_plan_repository import (
    RollbackPlanRepository,
)
from src.domain.value_objects.rollback_plan_id import (
    RollbackPlanId,
)
from src.infrastructure.adapters.rollback_plan_mapper import (
    RollbackPlanMapper,
)
from src.infrastructure.database.models.rollback_plan_model import (
    RollbackPlanModel,
)


class RollbackPlanRepositorySQLAlchemy(
    RollbackPlanRepository,
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        rollback_plan: RollbackPlan,
    ) -> None:

        model = RollbackPlanMapper.to_model(
            rollback_plan
        )

        self._session.add(
            model
        )

        await self._session.commit()

    async def get_by_id(
        self,
        rollback_plan_id: RollbackPlanId,
    ) -> RollbackPlan | None:

        stmt = select(
            RollbackPlanModel
        ).where(
            RollbackPlanModel.rollback_plan_id
            == str(
                rollback_plan_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return RollbackPlanMapper.to_domain(
            model
        )