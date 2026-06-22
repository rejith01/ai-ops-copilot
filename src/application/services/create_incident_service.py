from src.domain.interfaces.incident_repository import (
    IncidentRepository,
)


class CreateIncidentService:

    def __init__(
        self,
        repository: IncidentRepository,
    ):
        self._repository = repository