from uuid import UUID

from src.domain.entities.root_cause_hypothesis import (
    RootCauseHypothesis,
)
from src.domain.value_objects.hypothesis_id import (
    HypothesisId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)
from src.infrastructure.database.models.root_cause_hypothesis_model import (
    RootCauseHypothesisModel,
)


class HypothesisMapper:

    @staticmethod
    def to_model(
        hypothesis: RootCauseHypothesis,
    ) -> RootCauseHypothesisModel:

        return RootCauseHypothesisModel(
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

    @staticmethod
    def to_domain(
        model: RootCauseHypothesisModel,
    ) -> RootCauseHypothesis:

        return RootCauseHypothesis(
            hypothesis_id=HypothesisId(
                UUID(
                    model.hypothesis_id
                )
            ),
            investigation_id=InvestigationId(
                UUID(
                    model.investigation_id
                )
            ),
            description=model.description,
            confidence_score=model.confidence_score,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )