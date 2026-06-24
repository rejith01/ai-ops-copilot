from datetime import datetime
from uuid import UUID
from uuid import uuid4

from src.application.commands.create_evidence_command import (
    CreateEvidenceCommand,
)
from src.application.dto.evidence_dto import (
    EvidenceDTO,
)
from src.domain.entities.evidence import (
    Evidence,
)
from src.domain.interfaces.evidence_repository import (
    EvidenceRepository,
)
from src.domain.value_objects.evidence_id import (
    EvidenceId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)


class CreateEvidenceService:

    def __init__(
        self,
        repository: EvidenceRepository,
    ):
        self._repository = repository

    async def execute(
        self,
        command: CreateEvidenceCommand,
    ) -> EvidenceDTO:

        now = datetime.utcnow()

        evidence = Evidence(
            evidence_id=EvidenceId(
                uuid4()
            ),
            investigation_id=InvestigationId(
                UUID(
                    command.investigation_id
                )
            ),
            source=command.source,
            content=command.content,
            confidence_score=command.confidence_score,
            status="COLLECTED",
            created_at=now,
            updated_at=now,
        )

        await self._repository.save(
            evidence
        )

        return EvidenceDTO(
            evidence_id=str(
                evidence.evidence_id.value
            ),
            investigation_id=str(
                evidence.investigation_id.value
            ),
            source=evidence.source,
            content=evidence.content,
            confidence_score=evidence.confidence_score,
            status=evidence.status,
            created_at=evidence.created_at,
            updated_at=evidence.updated_at,
        )