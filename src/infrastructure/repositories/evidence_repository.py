from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.evidence import (
    Evidence,
)
from src.domain.interfaces.evidence_repository import (
    EvidenceRepository,
)
from src.domain.value_objects.evidence_id import (
    EvidenceId,
)
from src.infrastructure.adapters.evidence_mapper import (
    EvidenceMapper,
)
from src.infrastructure.database.models.evidence_model import (
    EvidenceModel,
)


class EvidenceRepositorySQLAlchemy(
    EvidenceRepository,
):

    def __init__(
        self,
        session: AsyncSession,
    ):
        self._session = session

    async def save(
        self,
        evidence: Evidence,
    ) -> None:

        model = EvidenceMapper.to_model(
            evidence
        )

        self._session.add(
            model
        )

        await self._session.commit()

    async def get_by_id(
        self,
        evidence_id: EvidenceId,
    ) -> Evidence | None:

        stmt = select(
            EvidenceModel
        ).where(
            EvidenceModel.evidence_id
            == str(
                evidence_id.value
            )
        )

        result = await self._session.execute(
            stmt
        )

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return EvidenceMapper.to_domain(
            model
        )