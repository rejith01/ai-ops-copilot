from uuid import UUID

from src.domain.entities.incident import Incident
from src.domain.value_objects.incident_id import IncidentId
from src.infrastructure.database.models.incident_model import IncidentModel


class IncidentMapper:

    @staticmethod
    def to_model(
        incident: Incident,
    ) -> IncidentModel:
        return IncidentModel(
            incident_id=str(
                incident.incident_id.value
            ),
            title=incident.title,
            description=incident.description,
            service_name=incident.service_name,
            severity=incident.severity,
            status=incident.status,
            created_at=incident.created_at,
            updated_at=incident.updated_at,
        )

    @staticmethod
    def to_domain(
        model: IncidentModel,
    ) -> Incident:
        return Incident(
            incident_id=IncidentId(
                UUID(model.incident_id)
            ),
            title=model.title,
            description=model.description,
            service_name=model.service_name,
            severity=model.severity,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )