from uuid import UUID

from src.domain.entities.investigation import (
    Investigation,
)
from src.domain.value_objects.incident_id import (
    IncidentId,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)
from src.infrastructure.database.models.investigation_model import (
    InvestigationModel,
)


class InvestigationMapper:

    @staticmethod
    def to_model(
        investigation: Investigation,
    ) -> InvestigationModel:

        return InvestigationModel(
            investigation_id=str(
                investigation.investigation_id.value
            ),
            incident_id=str(
                investigation.incident_id.value
            ),
            status=investigation.status,
            created_at=investigation.created_at,
            updated_at=investigation.updated_at,
        )

    @staticmethod
    def to_domain(
        model: InvestigationModel,
    ) -> Investigation:

        return Investigation(
            investigation_id=InvestigationId(
                UUID(
                    model.investigation_id
                )
            ),
            incident_id=IncidentId(
                UUID(
                    model.incident_id
                )
            ),
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )