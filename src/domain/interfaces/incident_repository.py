from abc import ABC
from abc import abstractmethod

from src.domain.entities.incident import Incident
from src.domain.value_objects.incident_id import IncidentId


class IncidentRepository(ABC):

    @abstractmethod
    async def save(
        self,
        incident: Incident,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        incident_id: IncidentId,
    ) -> Incident | None:
        pass