from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.incident import Incident
from src.domain.interfaces.incident_repository import IncidentRepository
from src.domain.value_objects.incident_id import IncidentId
from src.infrastructure.adapters.incident_mapper import IncidentMapper
from src.infrastructure.database.models.incident_model import IncidentModel


class IncidentRepositorySQLAlchemy(
    IncidentRepository
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        incident: Incident,
    ) -> None:

        model = IncidentMapper.to_model(
            incident
        )

        self._session.add(model)

        await self._session.commit()

    async def get_by_id(
        self,
        incident_id: IncidentId,
    ) -> Incident | None:

        stmt = select(
            IncidentModel
        ).where(
            IncidentModel.incident_id
            == str(
                incident_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return IncidentMapper.to_domain(
            model
        )