from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.investigation import (
    Investigation,
)
from src.domain.interfaces.investigation_repository import (
    InvestigationRepository,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)
from src.infrastructure.adapters.investigation_mapper import (
    InvestigationMapper,
)
from src.infrastructure.database.models.investigation_model import (
    InvestigationModel,
)


class InvestigationRepositorySQLAlchemy(
    InvestigationRepository,
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        investigation: Investigation,
    ) -> None:

        model = InvestigationMapper.to_model(
            investigation
        )

        self._session.add(
            model
        )

        await self._session.commit()

    async def get_by_id(
        self,
        investigation_id: InvestigationId,
    ) -> Investigation | None:

        stmt = select(
            InvestigationModel
        ).where(
            InvestigationModel.investigation_id
            == str(
                investigation_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return InvestigationMapper.to_domain(
            model
        )