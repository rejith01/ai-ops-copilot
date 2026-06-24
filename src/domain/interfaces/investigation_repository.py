from abc import ABC
from abc import abstractmethod

from src.domain.entities.investigation import (
    Investigation,
)
from src.domain.value_objects.investigation_id import (
    InvestigationId,
)


class InvestigationRepository(
    ABC,
):

    @abstractmethod
    async def save(
        self,
        investigation: Investigation,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        investigation_id: InvestigationId,
    ) -> Investigation | None:
        pass