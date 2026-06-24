from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.root_cause_hypothesis import (
    RootCauseHypothesis,
)
from src.domain.interfaces.hypothesis_repository import (
    HypothesisRepository,
)
from src.domain.value_objects.hypothesis_id import (
    HypothesisId,
)
from src.infrastructure.adapters.hypothesis_mapper import (
    HypothesisMapper,
)
from src.infrastructure.database.models.root_cause_hypothesis_model import (
    RootCauseHypothesisModel,
)


class HypothesisRepositorySQLAlchemy(
    HypothesisRepository,
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        hypothesis: RootCauseHypothesis,
    ) -> None:

        model = HypothesisMapper.to_model(
            hypothesis
        )

        self._session.add(
            model
        )

        await self._session.commit()

    async def get_by_id(
        self,
        hypothesis_id: HypothesisId,
    ) -> RootCauseHypothesis | None:

        stmt = select(
            RootCauseHypothesisModel
        ).where(
            RootCauseHypothesisModel.hypothesis_id
            == str(
                hypothesis_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return HypothesisMapper.to_domain(
            model
        )