from datetime import datetime
from uuid import UUID
from uuid import uuid4

from src.application.commands.create_hypothesis_command import (
    CreateHypothesisCommand,
)
from src.application.dto.hypothesis_dto import (
    HypothesisDTO,
)
from src.domain.entities.root_cause_hypothesis import (
    RootCauseHypothesis,
)
from src.domain.interfaces.hypothesis_repository import (
    HypothesisRepository,
)
from src.domain.value_objects.hypothesis_id import (
    HypothesisId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)


class CreateHypothesisService:

    def __init__(
        self,
        repository: HypothesisRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateHypothesisCommand,
    ) -> HypothesisDTO:

        now = datetime.utcnow()

        hypothesis = RootCauseHypothesis(
            hypothesis_id=HypothesisId(
                uuid4()
            ),
            investigation_id=InvestigationId(
                UUID(
                    command.investigation_id
                )
            ),
            description=command.description,
            confidence_score=command.confidence_score,
            status="GENERATED",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            hypothesis
        )

        return HypothesisDTO(
            hypothesis_id=str(
                hypothesis.hypothesis_id.value
            ),
            investigation_id=str(
                hypothesis.investigation_id.value
            ),
            description=hypothesis.description,
            confidence_score=hypothesis.confidence_score,
            status=hypothesis.status,
            created_at=hypothesis.created_at,
            updated_at=hypothesis.updated_at,
        )