from uuid import UUID

from src.domain.entities.evidence import (
    Evidence,
)
from src.domain.value_objects.evidence_id import (
    EvidenceId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)
from src.infrastructure.database.models.evidence_model import (
    EvidenceModel,
)


class EvidenceMapper:

    @staticmethod
    def to_model(
        evidence: Evidence,
    ) -> EvidenceModel:

        return EvidenceModel(
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

    @staticmethod
    def to_domain(
        model: EvidenceModel,
    ) -> Evidence:

        return Evidence(
            evidence_id=EvidenceId(
                UUID(
                    model.evidence_id
                )
            ),
            investigation_id=InvestigationId(
                UUID(
                    model.investigation_id
                )
            ),
            source=model.source,
            content=model.content,
            confidence_score=model.confidence_score,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )