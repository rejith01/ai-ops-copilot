from abc import ABC
from abc import abstractmethod

from src.domain.entities.evidence import (
    Evidence,
)
from src.domain.value_objects.evidence_id import (
    EvidenceId,
)


class EvidenceRepository(
    ABC,
):

    @abstractmethod
    async def save(
        self,
        evidence: Evidence,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        evidence_id: EvidenceId,
    ) -> Evidence | None:
        pass